import logging
from flask import Blueprint, jsonify
from utils import get_posts_all, get_post_by_pk


api_blueprint = Blueprint('api_blueprint', __name__, template_folder='templates', url_prefix='/')

api_logger = logging.getLogger('api_logger')


@api_blueprint.route('/api/posts')
def get_json_posts():
    posts = get_posts_all()
    api_logger.info('Запрос /api/posts')
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>')
def get_json_post(post_id):
    post = get_post_by_pk(post_id)
    api_logger.info(f'Запроc /api/posts/{post_id}')
    return jsonify(post)
