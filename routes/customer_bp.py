from flask import Blueprint
from controllers.customerController import index, store, show, update, destroy

customer_bp = Blueprint('customer_bp', __name__)

customer_bp.route('/', methods=['GET'])(index)
customer_bp.route('/create', methods=['POST'])(store)
customer_bp.route('/<int:customer_id>', methods=['GET'])(show)
customer_bp.route('/<int:customer_id>/edit', methods=['POST'])(update)
customer_bp.route('/<int:customer_id>', methods=['DELETE'])(destroy)