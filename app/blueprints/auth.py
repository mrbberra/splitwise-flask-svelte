import functools
from flask import Blueprint, redirect, request, session, url_for, g
from ..lib.splitwise import get_splitwise

bp = Blueprint('auth', __name__, url_prefix='/auth')

def redirect_uri():
  return url_for('auth.callback', _external=True)

@bp.route('/login', methods=['GET'])
def login():
  url, state = get_splitwise().getOAuth2AuthorizeURL(redirect_uri())
  session['state'] = state
  return redirect(url)

@bp.route('/oauth', methods=['GET'])
def callback():
  if request.args.get('state') != session['state']:
    return 'Invalid state', 400

  code = request.args.get('code')
  access_token = get_splitwise().getOAuth2AccessToken(code, redirect_uri())
  session['access_token'] = access_token
  return redirect(url_for('index'))

@bp.route('/logout')
def logout():
  session.clear()
  return redirect(url_for('index'))

def login_required(view):
  @functools.wraps(view)
  def wrapped_view(**kwargs):
    if 'access_token' not in session:
      return redirect(url_for('auth.login'))
    if g.user is None:
      access_token = session['access_token']
      get_splitwise().setOAuth2AccessToken(access_token)
      g.user = get_splitwise().getCurrentUser()
    return view(**kwargs)
  return wrapped_view
