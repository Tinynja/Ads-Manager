import os
from flask import Blueprint, Flask, jsonify, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

env = os.environ.get('FLASK_ENV', 'dev')

# Initialize Flask, API and database
app = Flask(__name__)
app.config.from_object(f'config.{env.capitalize()}Config')

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint, prefix='/api')

db = SQLAlchemy(app)

# Register blueprint
app.register_blueprint(api_blueprint)


# Register resources

# Error handlers
@app.errorhandler(404)
def not_found(error):
    message = {
        'status': 404,
        'message': 'Page not found',
        'url': request.url
    }
    response = jsonify(message)
    response.status_code = 404
    return response
