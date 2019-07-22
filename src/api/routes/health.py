from flask import Blueprint, jsonify
health_api = Blueprint('health_api', __name__)

@health_api.route('/health')
def health():
    return jsonify(status='OK')

@health_api.route('/info')
def info():
    return jsonify(version='v1.0.0')
