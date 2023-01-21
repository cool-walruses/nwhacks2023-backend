import os
import openai
from flask import Flask

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# a simple page that says hello
@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
