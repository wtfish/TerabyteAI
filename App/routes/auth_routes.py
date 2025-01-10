from flask import Blueprint
from App.controllers.auth_controller import login

auth_bp = Blueprint('auth_bp', __name__)

# Login route
auth_bp.route('/login', methods=['GET', 'POST'])(login)
