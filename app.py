import os
import openai
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    openai.api_key = os.getenv("OPENAI_API_KEY")

    from flaskapp import generator

    # a simple page that says hello
    @app.route('/test')
    def hello():
        return 'Hello, World!'

    app.register_blueprint(generator.bp)
    return app

app = create_app()
if __name__ == '__main__':
    app.run()
