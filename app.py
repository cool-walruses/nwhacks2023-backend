import os
import openai
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    """
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    """

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    @app.route('/openai')
    def openAiHandler():
        request = "\"\"\"\nA function that does insertion sort.\n\"\"\""
        openai.api_key = "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"
        return openai.Completion.create(model="code-cushman-001", prompt=request, temperature=0.2, max_tokens=1024)

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
