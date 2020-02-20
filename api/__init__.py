from flask import Blueprint, Flask, jsonify, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# Init Flask and FlaskRestful
app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/api')

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/ads_manager.db'
db = SQLAlchemy(app)

# Register blueprint
app.register_blueprint(api_bp)

# Register resources

# Error handlers
@app.errorhandler(404)
def not_found(error=None):
    message = {
      'status': 404,
      'message': 'Page not found',
      'url': request.url
    }
    response = jsonify(message)
    response.status_code = 404
    return response
