from flask import Blueprint, render_template, request
from utils import get_posts_by_user


user_blueprint = Blueprint('user_blueprint', __name__, template_folder='templates', url_prefix='/')


@user_blueprint.route('/user/<username>')
def user_page(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts)