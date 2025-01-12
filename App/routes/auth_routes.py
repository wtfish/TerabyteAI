from flask import Blueprint
from App.controllers.auth_controller import login
from App.controllers.dashboard_controller import index

auth_bp = Blueprint('auth_bp', __name__)
dashboard_bp = Blueprint('dashboard_bp', __name__)

# Login route
auth_bp.route('/login', methods=['GET', 'POST'])(login)
# auth_bp.route('/index', methods=['GET'])(index)
dashboard_bp.route('/dashboard', methods=['GET'])(index)
