from flask import Blueprint, render_template, request
from utils import get_posts_all, search_for_posts


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates', url_prefix='/')


@main_blueprint.route('/')
def main_index():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@main_blueprint.route('/search')
def search_page():
    substr = request.args.get('s')
    posts, posts_counter = search_for_posts(substr)
    return render_template('search.html', substr=substr, posts=posts, posts_counter=posts_counter)
