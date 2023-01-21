import openai
import flaskapp.constants as const
from http import HTTPStatus
from flask import Blueprint, jsonify, request

bp = Blueprint('generator', __name__, url_prefix='/generator')

@bp.route('/generate', methods=['POST'])
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
            source_language : string
            prompt : string

        
            SUCCESS (200)
            =============
            The code generation was successful.

            Body Data (Key : Datatype)
            --------------------------
                code : string
        
        """
        # Get information from request
        programming_language = request.form['programming_language']
        source_language = request.form['language']
        prompt = request.form['prompt']

        # Make request to openai API
        response = openai.Completion.create(
            model=const.CODEX_MODEL,
            prompt=generate_code_prompt(programming_language, prompt),
            temperature=const.TEMPERATURE,
            max_tokens=const.MAX_TOKENS
        )

        return jsonify({'code', response.text}), HTTPStatus.OK

def generate_code_prompt(programming_language, prompt):
    return "\n".join(
            const.LANG_CONSTANTS[programming_language].startToken,
            f"In {programming_language}, {prompt}",
            const.LANG_CONSTANTS[programming_language].endToken
        )
