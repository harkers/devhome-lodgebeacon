"""
Display Forge - Database Initialization
Creates SQLite database with all tables and indexes
"""

import os
import sys
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.models import db, Setting
from backend.app import create_app

def init_db():
    """Initialize database with all tables"""
    app = create_app()
    
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Create default settings if they don't exist
        default_settings = {
            'hall_name': 'Your Masonic Hall',
            'hall_address': 'Your Address Here',
            'slide_interval_seconds': '10',
            'default_theme': 'masonic',
            'calendar_sync_interval': '15',
            'display_start_days_before': '7'
        }
        
        for key, value in default_settings.items():
            existing = Setting.query.filter_by(key=key).first()
            if not existing:
                setting = Setting(key=key, value=value)
                db.session.add(setting)
                print(f"✓ Created setting: {key}")
        
        db.session.commit()
        
        # Show database location
        db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'display-forge.db')
        print(f"\n✅ Database initialized at: {db_path}")
        print(f"📊 Tables created: notices, calendar_sources, settings, displays")
        print(f"⚙️  Default settings added")

if __name__ == '__main__':
    init_db()
