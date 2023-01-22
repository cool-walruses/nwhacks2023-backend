import openai
import flaskapp.helpers.constants as const
from flaskapp.helpers.translation import generate_response
from flaskapp.helpers.exceptions import IllegalContentError
from http import HTTPStatus
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

bp = Blueprint('generator', __name__, url_prefix='/generator')

@bp.route('/generate', methods=['POST'])
@cross_origin()
def generate():
    if request.method == 'POST':
        """
        URL: <api>/generator/generate

        POST REQUEST
        ============

            Given the programming language, source language, and prompt, generate code
            that the prompt specifies

            Body Data (Key : Datatype)
            ==========================
            programming_language : string
            prompt : string

        
            SUCCESS (200)
            =============
            The code generation was successful.

            Response Data (Key : Datatype)
            ------------------------------
                code : string

            FORBIDDEN (403)
            ===============
            Abusive content was submitted.

            Response Data (Key : Datatype)
            ------------------------------
                message : string
        """
        # Get information from request
        programming_language = request.json['programming_language'].title()
        prompt = request.json['prompt']

        try:
            response = generate_response(programming_language, prompt)
            code_content = response["choices"][0]["text"].strip()
            return jsonify(code=code_content), HTTPStatus.OK
        except IllegalContentError as err:
            return jsonify(message=err.message), HTTPStatus.FORBIDDEN
