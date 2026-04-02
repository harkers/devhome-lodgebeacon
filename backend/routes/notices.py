"""
Notices API - CRUD operations for display notices
"""

from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
import json

from backend.models import db, Notice

notices_bp = Blueprint('notices', __name__)


@notices_bp.route('', methods=['GET'])
def get_notices():
    """Get all notices with optional filtering"""
    status = request.args.get('status')
    source_type = request.args.get('source_type')
    
    query = Notice.query
    
    if status:
        query = query.filter(Notice.status == status)
    if source_type:
        query = query.filter(Notice.source_type == source_type)
    
    # Order by priority (high to low), then display_start
    query = query.order_by(Notice.priority.desc(), Notice.display_start.asc())
    
    notices = query.all()
    return jsonify([notice.to_dict() for notice in notices])


@notices_bp.route('/active', methods=['GET'])
def get_active_notices():
    """Get currently active notices (within display window and live status)"""
    now = datetime.utcnow()
    
    active = Notice.query.filter(
        Notice.status == 'live',
        Notice.display_start <= now,
        Notice.display_end >= now
    ).order_by(Notice.priority.desc()).all()
    
    return jsonify([notice.to_dict() for notice in active])


@notices_bp.route('', methods=['POST'])
def create_notice():
    """Create a new notice"""
    data = request.json
    
    if not data or not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400
    
    # Parse dates
    display_start = datetime.fromisoformat(data['display_start']) if data.get('display_start') else datetime.utcnow()
    display_end = datetime.fromisoformat(data['display_end']) if data.get('display_end') else display_start + timedelta(hours=2)
    
    notice = Notice(
        source_type=data.get('source_type', 'manual'),
        source_id=data.get('source_id'),
        title=data['title'],
        body=data.get('body'),
        category=data.get('category'),
        event_start=datetime.fromisoformat(data['event_start']) if data.get('event_start') else None,
        event_end=datetime.fromisoformat(data['event_end']) if data.get('event_end') else None,
        display_start=display_start,
        display_end=display_end,
        priority=data.get('priority', 0),
        status=data.get('status', 'scheduled'),
        target_display=data.get('target_display', 'all'),
        sync_metadata=json.dumps(data.get('sync_metadata')) if data.get('sync_metadata') else None
    )
    
    db.session.add(notice)
    db.session.commit()
    
    # Emit WebSocket event
    from flask import current_app
    socketio = current_app.extensions.get('socketio')
    if socketio:
        socketio.emit('notice_created', notice.to_dict())
    
    return jsonify(notice.to_dict()), 201


@notices_bp.route('/<int:id>', methods=['GET'])
def get_notice(id):
    """Get a single notice by ID"""
    notice = Notice.query.get_or_404(id)
    return jsonify(notice.to_dict())


@notices_bp.route('/<int:id>', methods=['PUT'])
def update_notice(id):
    """Update an existing notice"""
    notice = Notice.query.get_or_404(id)
    data = request.json
    
    # Update fields
    if 'title' in data:
        notice.title = data['title']
    if 'body' in data:
        notice.body = data['body']
    if 'category' in data:
        notice.category = data['category']
    if 'priority' in data:
        notice.priority = data['priority']
    if 'status' in data:
        notice.status = data['status']
    if 'display_start' in data:
        notice.display_start = datetime.fromisoformat(data['display_start'])
    if 'display_end' in data:
        notice.display_end = datetime.fromisoformat(data['display_end'])
    if 'target_display' in data:
        notice.target_display = data['target_display']
    
    notice.updated_at = datetime.utcnow()
    db.session.commit()
    
    # Emit WebSocket event
    from flask import current_app
    socketio = current_app.extensions.get('socketio')
    if socketio:
    socketio.emit('notice_updated', notice.to_dict())
    
    return jsonify(notice.to_dict())


@notices_bp.route('/<int:id>', methods=['DELETE'])
def delete_notice(id):
    """Delete a notice"""
    notice = Notice.query.get_or_404(id)
    db.session.delete(notice)
    db.session.commit()
    
    # Emit WebSocket event
    from flask import current_app
    socketio = current_app.extensions.get('socketio')
    if socketio:
    socketio.emit('notice_deleted', {'id': id})
    
    return '', 204


@notices_bp.route('/<int:id>/suppress', methods=['POST'])
def suppress_notice(id):
    """Suppress a notice (hide without deleting)"""
    notice = Notice.query.get_or_404(id)
    notice.status = 'suppressed'
    db.session.commit()
    
    from flask import current_app
    socketio = current_app.extensions.get('socketio')
    if socketio:
    socketio.emit('notice_updated', notice.to_dict())
    
    return jsonify(notice.to_dict())


@notices_bp.route('/<int:id>/restore', methods=['POST'])
def restore_notice(id):
    """Restore a suppressed notice"""
    notice = Notice.query.get_or_404(id)
    notice.status = 'live'
    db.session.commit()
    
    from flask import current_app
    socketio = current_app.extensions.get('socketio')
    if socketio:
    socketio.emit('notice_updated', notice.to_dict())
    
    return jsonify(notice.to_dict())
