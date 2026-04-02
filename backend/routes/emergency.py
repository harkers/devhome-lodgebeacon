"""
Emergency API - Broadcast emergency messages
"""

from flask import Blueprint, request, jsonify, current_app
from datetime import datetime

from backend.models import db, Notice

emergency_bp = Blueprint('emergency', __name__)


@emergency_bp.route('', methods=['POST'])
def send_emergency():
    """Send emergency broadcast to all displays"""
    data = request.json
    
    if not data or not data.get('message'):
        return jsonify({'error': 'Message is required'}), 400
    
    # Create emergency notice with highest priority
    duration_minutes = data.get('duration', 60)  # Default 1 hour
    
    emergency = Notice(
        source_type='manual',
        title='⚠️ Emergency Notice',
        body=data['message'],
        category='emergency',
        display_start=datetime.utcnow(),
        display_end=datetime.utcnow() + timedelta(minutes=duration_minutes),
        priority=999,  # Highest priority
        status='live',
        target_display='all'
    )
    
    db.session.add(emergency)
    db.session.commit()
    
    # Emit WebSocket event for immediate display
    socketio = current_app.extensions.get('socketio')
    if socketio:
        socketio.emit('emergency_broadcast', {
            'type': 'emergency',
            'message': data['message'],
            'active': True,
            'timestamp': datetime.utcnow().isoformat()
        })
    
    return jsonify({
        'status': 'sent',
        'notice_id': emergency.id,
        'expires_at': emergency.display_end.isoformat()
    }), 201


@emergency_bp.route('/clear', methods=['POST'])
def clear_emergency():
    """Clear active emergency notices"""
    now = datetime.utcnow()
    
    # Find and expire all active emergencies
    emergencies = Notice.query.filter(
        Notice.status == 'live',
        Notice.category == 'emergency',
        Notice.display_end > now
    ).all()
    
    for emergency in emergencies:
        emergency.display_end = now
        emergency.status = 'expired'
    
    db.session.commit()
    
    # Emit WebSocket event
    socketio = current_app.extensions.get('socketio')
    if socketio:
        socketio.emit('emergency_broadcast', {
            'type': 'emergency',
            'active': False,
            'timestamp': datetime.utcnow().isoformat()
        })
    
    return jsonify({'status': 'cleared', 'count': len(emergencies)})


@emergency_bp.route('/status', methods=['GET'])
def emergency_status():
    """Check if emergency is currently active"""
    now = datetime.utcnow()
    
    active = Notice.query.filter(
        Notice.status == 'live',
        Notice.category == 'emergency',
        Notice.display_start <= now,
        Notice.display_end > now
    ).first()
    
    if active:
        return jsonify({
            'active': True,
            'message': active.body,
            'started_at': active.display_start.isoformat(),
            'expires_at': active.display_end.isoformat()
        })
    else:
        return jsonify({'active': False})
