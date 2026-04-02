"""
Display Forge - Database Models
SQLite-based storage for notices, calendar events, and settings
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Notice(db.Model):
    """Manual and calendar-driven notices"""
    __tablename__ = 'notices'
    
    id = db.Column(db.Integer, primary_key=True)
    source_type = db.Column(db.Text, nullable=False)  # 'manual' or 'calendar'
    source_id = db.Column(db.Text)  # External ID (e.g., Google Calendar event ID)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text)
    category = db.Column(db.Text)
    event_start = db.Column(db.DateTime)  # Actual event start
    event_end = db.Column(db.DateTime)  # Actual event end
    display_start = db.Column(db.DateTime, nullable=False)  # When to show
    display_end = db.Column(db.DateTime, nullable=False)  # When to hide
    priority = db.Column(db.Integer, default=0)
    status = db.Column(db.Text, default='scheduled')  # draft, scheduled, live, expired, suppressed
    target_display = db.Column(db.Text, default='all')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    sync_metadata = db.Column(db.Text)  # JSON string for calendar sync info
    
    def to_dict(self):
        return {
            'id': self.id,
            'source_type': self.source_type,
            'source_id': self.source_id,
            'title': self.title,
            'body': self.body,
            'category': self.category,
            'event_start': self.event_start.isoformat() if self.event_start else None,
            'event_end': self.event_end.isoformat() if self.event_end else None,
            'display_start': self.display_start.isoformat() if self.display_start else None,
            'display_end': self.display_end.isoformat() if self.display_end else None,
            'priority': self.priority,
            'status': self.status,
            'target_display': self.target_display,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


class CalendarSource(db.Model):
    """External calendar sources"""
    __tablename__ = 'calendar_sources'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    source_type = db.Column(db.Text, nullable=False)  # google, microsoft, ics
    url = db.Column(db.Text)  # For ICS feeds
    calendar_id = db.Column(db.Text)  # For Google/Microsoft
    sync_interval_minutes = db.Column(db.Integer, default=15)
    last_sync = db.Column(db.DateTime)
    sync_status = db.Column(db.Text, default='pending')  # pending, success, error
    sync_error = db.Column(db.Text)
    enabled = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'source_type': self.source_type,
            'url': self.url,
            'calendar_id': self.calendar_id,
            'sync_interval_minutes': self.sync_interval_minutes,
            'last_sync': self.last_sync.isoformat() if self.last_sync else None,
            'sync_status': self.sync_status,
            'sync_error': self.sync_error,
            'enabled': self.enabled
        }


class Setting(db.Model):
    """Application settings"""
    __tablename__ = 'settings'
    
    key = db.Column(db.Text, primary_key=True)
    value = db.Column(db.Text, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'key': self.key,
            'value': self.value,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


class Display(db.Model):
    """Registered display devices"""
    __tablename__ = 'displays'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text)
    theme = db.Column(db.Text, default='masonic')
    is_active = db.Column(db.Boolean, default=True)
    last_seen = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'theme': self.theme,
            'is_active': self.is_active,
            'last_seen': self.last_seen.isoformat() if self.last_seen else None
        }
