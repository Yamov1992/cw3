import json


def get_posts_all(path='data/posts.json'):
    """
    Возвращает все посты, загруженные из файла json
    """
    try:
        with open(path, encoding="utf-8") as file:
            posts = json.load(file)
        return posts
    except FileNotFoundError:
        print("Файл не найден")


def get_posts_by_user(user_name):
    """
    Возвращает посты по идентификатору пользователя
    """
    posts = get_posts_all()
    user_posts = []
    counter = 0
    for post in posts:
        if user_name.title() == post["poster_name"].title():
            user_posts.append(post)
            counter += 1
    return user_posts, counter


def get_comments_by_post_id(post_id, path="data/comments.json"):
    """
    Возвращает комментарии по идентификатору поста
    """
    with open(path, encoding="utf-8") as file:
        comments_data = json.load(file)
    comments = []
    comments_counter = 0
    for comment in comments_data:
        if post_id == comment["post_id"]:
            comments.append(comment)
            comments_counter += 1
    return comments, comments_counter


def search_for_posts(query):
    """
     Возвращает список постов и их счетчик постов по ключевому слову
    """
    posts = get_posts_all()
    post_counter = 0
    query_post = []
    for post in posts:
        if query.title() in post["content"].title():
            query_post.append(post)
            post_counter += 1
    return query_post, post_counter


def get_post_by_pk(pk):
    """
    Возвращает один пост по его идентификатору
    """
    posts = get_posts_all()
    for post in posts:
        if pk == post["pk"]:
            return post






