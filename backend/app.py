"""
Display Forge - Main Application
Flask backend with SQLite storage and WebSocket support
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from datetime import datetime, timedelta
import json

from backend.models import db, Notice, CalendarSource, Setting, Display


def create_app():
    """Application factory"""
    app = Flask(__name__, static_folder='../frontend', static_url_path='')
    
    # Configuration
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, "data", "display-forge.db")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'display-forge-dev-key-change-in-production')
    
    # Initialize extensions
    db.init_app(app)
    CORS(app)
    socketio = SocketIO(app, cors_allowed_origins="*")
    
    # Store socketio instance for use in routes
    app.socketio = socketio
    
    # Register routes
    from backend.routes.notices import notices_bp
    from backend.routes.calendar import calendar_bp
    from backend.routes.settings import settings_bp
    from backend.routes.emergency import emergency_bp
    
    app.register_blueprint(notices_bp, url_prefix='/api/notices')
    app.register_blueprint(calendar_bp, url_prefix='/api/calendar')
    app.register_blueprint(settings_bp, url_prefix='/api/settings')
    app.register_blueprint(emergency_bp, url_prefix='/api/emergency')
    
    # Serve frontend
    @app.route('/')
    def serve_display():
        return send_from_directory(app.static_folder, 'display.html')
    
    @app.route('/admin.html')
    def serve_admin():
        return send_from_directory(app.static_folder, 'admin.html')
    
    @app.route('/css/<path:filename>')
    def serve_css(filename):
        return send_from_directory(os.path.join(app.static_folder, 'css'), filename)
    
    @app.route('/js/<path:filename>')
    def serve_js(filename):
        return send_from_directory(os.path.join(app.static_folder, 'js'), filename)
    
    # Health check
    @app.route('/api/health')
    def health():
        return jsonify({
            'status': 'ok',
            'service': 'display-forge-api',
            'timestamp': datetime.utcnow().isoformat()
        })
    
    # WebSocket events
    @socketio.on('connect')
    def handle_connect():
        print(f'Client connected: {request.sid}')
    
    @socketio.on('disconnect')
    def handle_disconnect():
        print(f'Client disconnected: {request.sid}')
    
    @socketio.on('register_display')
    def handle_register(data):
        """Register a display device"""
        display_name = data.get('name', 'Unknown Display')
        # Could save to database here
        
    # Scheduler for auto-expiry
    from apscheduler.schedulers.background import BackgroundScheduler
    
    scheduler = BackgroundScheduler()
    
    def check_expired_notices():
        """Mark expired notices automatically"""
        with app.app_context():
            now = datetime.utcnow()
            expired = Notice.query.filter(
                Notice.status == 'live',
                Notice.display_end < now
            ).all()
            
            for notice in expired:
                notice.status = 'expired'
            
            if expired:
                db.session.commit()
                socketio.emit('notices_updated', {'count': len(expired)})
                print(f"✓ Expired {len(expired)} notices")
    
    scheduler.add_job(check_expired_notices, 'interval', minutes=5)
    scheduler.start()
    
    return app


if __name__ == '__main__':
    app = create_app()
    socketio = app.extensions['socketio']
    print("🚀 Starting Display Forge API on http://0.0.0.0:5001")
    socketio.run(app, host='0.0.0.0', port=5001, debug=True, allow_unsafe_werkzeug=True)
