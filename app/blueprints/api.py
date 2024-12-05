from flask import Blueprint, g, jsonify
from .auth import login_required
from ..lib.splitwise import get_splitwise

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/me', methods=['GET'])
@login_required
def me():
  user = g.user
  groups = get_splitwise().getGroups()
  def format_group(group):
    return { 'name': group.getName(), 'id': group.getId() }
  formatted_groups = list(map(format_group, groups))
  return jsonify({
    'id': user.getId(),
    'firstName': user.getFirstName(),
    'lastName': user.getLastName(),
    'email': user.getEmail(),
    'groups': formatted_groups
  })

@bp.route('/upload', methods=['POST'])
@login_required
def upload():
  return jsonify({ 'message': 'Upload successful' })
