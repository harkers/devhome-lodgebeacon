"""
Calendar API - Import and sync external calendars
"""

from flask import Blueprint, request, jsonify, current_app
from datetime import datetime, timedelta
import requests
from icalendar import Calendar as IcalCalendar
import json

from backend.models import db, Notice, CalendarSource

calendar_bp = Blueprint('calendar', __name__)


@calendar_bp.route('/sources', methods=['GET'])
def get_calendar_sources():
    """Get all configured calendar sources"""
    sources = CalendarSource.query.all()
    return jsonify([source.to_dict() for source in sources])


@calendar_bp.route('/sources', methods=['POST'])
def add_calendar_source():
    """Add a new calendar source"""
    data = request.json
    
    if not data or not data.get('name') or not data.get('source_type'):
        return jsonify({'error': 'Name and source_type are required'}), 400
    
    source = CalendarSource(
        name=data['name'],
        source_type=data['source_type'],
        url=data.get('url'),
        calendar_id=data.get('calendar_id'),
        sync_interval_minutes=data.get('sync_interval_minutes', 15)
    )
    
    db.session.add(source)
    db.session.commit()
    
    return jsonify(source.to_dict()), 201


@calendar_bp.route('/sources/<int:id>', methods=['DELETE'])
def remove_calendar_source(id):
    """Remove a calendar source"""
    source = CalendarSource.query.get_or_404(id)
    db.session.delete(source)
    db.session.commit()
    return '', 204


@calendar_bp.route('/sync', methods=['POST'])
def sync_calendars():
    """Trigger manual sync of all enabled calendar sources"""
    from flask import current_app
    socketio = current_app.extensions.get('socketio')
    if socketio:
    
    synced = []
    errors = []
    
    sources = CalendarSource.query.filter_by(enabled=True).all()
    
    for source in sources:
        try:
            if source.source_type == 'ics' and source.url:
                # Sync ICS feed
                count = sync_ics_feed(source)
                synced.append({'source': source.name, 'events': count})
            elif source.source_type == 'google':
                # Would implement Google Calendar API here
                errors.append({'source': source.name, 'error': 'Google Calendar not yet implemented'})
            elif source.source_type == 'microsoft':
                # Would implement Microsoft Graph API here
                errors.append({'source': source.name, 'error': 'Microsoft Calendar not yet implemented'})
            
            source.last_sync = datetime.utcnow()
            source.sync_status = 'success'
        except Exception as e:
            source.sync_status = 'error'
            source.sync_error = str(e)
            errors.append({'source': source.name, 'error': str(e)})
    
    db.session.commit()
    
    # Emit update
    if socketio:
        socketio.emit('calendar_synced', {'synced': synced, 'errors': errors})
    
    return jsonify({
        'synced': synced,
        'errors': errors,
        'total': len(synced) + len(errors)
    })


def sync_ics_feed(source):
    """Sync events from an ICS feed URL"""
    response = requests.get(source.url, timeout=30)
    response.raise_for_status()
    
    cal = IcalCalendar.from_ical(response.text)
    now = datetime.utcnow()
    future_end = now + timedelta(days=90)  # Import next 90 days
    
    count = 0
    display_start_days = int(get_display_start_days())
    
    for component in cal.walk():
        if component.name == 'VEVENT':
            dtstart = component.get('dtstart').dt if component.get('dtstart') else None
            dtend = component.get('dtend').dt if component.get('dtend') else None
            summary = str(component.get('summary', ''))
            description = str(component.get('description', ''))
            uid = str(component.get('uid', ''))
            
            if not dtstart:
                continue
            
            # Skip past events
            if dtstart < now:
                continue
            
            # Skip too-far-future events
            if dtstart > future_end:
                continue
            
            # Calculate display window
            display_start = dtstart - timedelta(days=display_start_days)
            display_end = dtend if dtend else dtstart + timedelta(hours=2)
            
            # Check if we already have this event
            existing = Notice.query.filter_by(
                source_type='calendar',
                source_id=uid
            ).first()
            
            if existing:
                # Update existing
                existing.title = summary
                existing.body = description[:500] if description else None
                existing.event_start = dtstart
                existing.event_end = dtend
                existing.display_start = display_start
                existing.display_end = display_end
                existing.status = 'scheduled' if display_start > now else 'live'
            else:
                # Create new
                notice = Notice(
                    source_type='calendar',
                    source_id=uid,
                    title=summary,
                    body=description[:500] if description else None,
                    event_start=dtstart,
                    event_end=dtend,
                    display_start=display_start,
                    display_end=display_end,
                    status='scheduled' if display_start > now else 'live',
                    sync_metadata=json.dumps({'calendar_source_id': source.id})
                )
                db.session.add(notice)
            
            count += 1
    
    return count


def get_display_start_days():
    """Get default display start days from settings"""
    from models import Setting
    setting = Setting.query.filter_by(key='display_start_days_before').first()
    return int(setting.value) if setting else 7
