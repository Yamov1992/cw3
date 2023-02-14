from flask import Flask, send_from_directory

from main.views import main_blueprint
from post.views import post_blueprint
from user.views import user_blueprint
from api.views import api_blueprint
from logger import config


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(api_blueprint)

config()

if __name__ == "__main__":
    app.run(debug=True)
