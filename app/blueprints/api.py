from flask import Blueprint, g, jsonify
from .auth import login_required
import sys

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/me', methods=['GET'])
@login_required
def me():
  user = g.user
  return jsonify({
    'id': user.getId(),
    'firstName': user.getFirstName(),
    'lastName': user.getLastName(),
    'email': user.getEmail(),
  })
