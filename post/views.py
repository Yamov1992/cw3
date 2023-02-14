from flask import Blueprint, render_template, request
from utils import get_post_by_pk, get_comments_by_post_id


post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates', url_prefix='/')


@post_blueprint.route('/post/<int:postid>')
def post_index(postid):
    post = get_post_by_pk(postid)
    comments, comments_counter = get_comments_by_post_id(postid)
    return render_template('post.html', post=post, comments=comments, comments_counter=comments_counter)