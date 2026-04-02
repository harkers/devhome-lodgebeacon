"""
Settings API - Application configuration
"""

from flask import Blueprint, request, jsonify
from datetime import datetime

from backend.models import db, Setting

settings_bp = Blueprint('settings', __name__)


@settings_bp.route('', methods=['GET'])
def get_settings():
    """Get all settings"""
    settings = Setting.query.all()
    return jsonify({s.key: s.value for s in settings})


@settings_bp.route('/<key>', methods=['GET'])
def get_setting(key):
    """Get a single setting by key"""
    setting = Setting.query.get_or_404(key)
    return jsonify(setting.to_dict())


@settings_bp.route('/<key>', methods=['PUT'])
def update_setting(key):
    """Update or create a setting"""
    data = request.json
    
    if not data or 'value' not in data:
        return jsonify({'error': 'Value is required'}), 400
    
    setting = Setting.query.filter_by(key=key).first()
    
    if setting:
        setting.value = data['value']
        setting.updated_at = datetime.utcnow()
    else:
        setting = Setting(key=key, value=data['value'])
        db.session.add(setting)
    
    db.session.commit()
    return jsonify(setting.to_dict())


@settings_bp.route('/bulk', methods=['PUT'])
def update_settings_bulk():
    """Update multiple settings at once"""
    data = request.json
    
    if not data:
        return jsonify({'error': 'No settings provided'}), 400
    
    updated = []
    for key, value in data.items():
        setting = Setting.query.filter_by(key=key).first()
        if setting:
            setting.value = str(value)
            setting.updated_at = datetime.utcnow()
        else:
            setting = Setting(key=key, value=str(value))
            db.session.add(setting)
        updated.append(key)
    
    db.session.commit()
    return jsonify({'updated': updated})
