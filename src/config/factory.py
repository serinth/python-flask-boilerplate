import logging
import sys
from flask import Flask, Blueprint
from flask import jsonify
from api.routes.health import namespace as health_api_ns, blueprint as health_api
from constants.http_responses import *
from flask_restx import Api


def create_app(config):
    blueprint = Blueprint('docs', __name__)

    api = Api(
        blueprint,
        title = 'Text Search Engine API',
        version = '1.0.0',
        description = 'All APIs related to Text Search for trademarks.'
    )
    
    api.add_namespace(health_api_ns)

    app = Flask(__name__)

    app.config.from_object(config)

    app.register_blueprint(health_api)
    app.register_blueprint(blueprint)
    # app.register_blueprint(<new_api_route>, url_prefix='/api')

    @app.after_request
    def add_header(response):
        return response

    @app.errorhandler(400)
    def bad_request(e):
        logging.error(e)
        return jsonify(errorCode=BAD_REQUEST_400['code'],
                errorDescription=BAD_REQUEST_400['message']), 400

    @app.errorhandler(500)
    def server_error(e):
        logging.error(e)
        return jsonify(errorCode=SERVER_ERROR_500['code'],
                errorDescription=SERVER_ERROR_500['message']), 500

    @app.errorhandler(404)
    def not_found(e):
        logging.error(e)
        return jsonify(errorCode=SERVER_ERROR_404['code'],
                errorDescription=SERVER_ERROR_404['message']), 404


    logging.basicConfig(stream=sys.stdout,
                        format='%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s',
                        level=logging.DEBUG)
    return app

