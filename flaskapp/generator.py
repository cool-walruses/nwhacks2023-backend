import openai
import flaskapp.constants as const
from http import HTTPStatus
from flask import Blueprint, jsonify, request

import pdb

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
        programming_language = request.json['programming_language'].title()
        source_language = request.json['source_language'].title()
        prompt = request.json['prompt']

        # Translate from source language
        if source_language != 'English':
            response = openai.Completion.create(
                prompt=generate_language_translation_prompt(source_language, prompt),
                **const.LANGUAGE_MODEL_PARAMS
            )
            prompt = response["choices"][0]["text"]

        # Make request to openai API
        response = openai.Completion.create(
            prompt=generate_code_prompt(programming_language, prompt),
            **const.CODEX_MODEL_PARAMS
        )

        # Translate back to original language if needed
        if source_language != 'English':
            response = openai.Completion.create(
                prompt=generate_code_language_translation_prompt(source_language, response["choices"][0]["text"]),
                **const.ENGLISH_TO_ORIGINAL_LANGUAGE_MODEL_PARAMS
            )

        code_content = response["choices"][0]["text"]

        #code_content = bytes(response["choices"][0]["text"], "utf-8").decode('unicode_escape')
        return jsonify(code=code_content), HTTPStatus.OK

def generate_language_translation_prompt(source_language, prompt):
    return "\n".join([
        f"Translate the following from {source_language} to English:",
        f"{prompt}"
    ])

def generate_code_language_translation_prompt(source_language, prompt):
    return "\n".join([
        f"Translate the comments, and variables into {source_language}:\n",
        f"{prompt}"
    ])

def generate_code_prompt(programming_language, prompt):
    return "\n".join([
            const.LANG_COMMENTS[programming_language].startToken,
            f"In {programming_language}, {prompt}",
            const.LANG_COMMENTS[programming_language].endToken
        ])
