from flask import Blueprint
from flask_restx import Namespace, Resource, fields

namespace = Namespace('metrics', description='Service metrics and health checks')

health_model = namespace.model('Health', {
    'status': fields.String
})

blueprint = Blueprint('health', __name__)

@namespace.route('/health')
class Health(Resource):
    @namespace.marshal_with(health_model)
    def get(self):
        return {'status': 'OK'}