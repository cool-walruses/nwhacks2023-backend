import openai
import flaskapp.helpers.constants as const
from flaskapp.helpers.exceptions import IllegalContentError

def generate_response(programming_language, source_language, prompt):

    # Check for abusive content
    content_check(prompt)
    print("HERE 1")

    # Translate from source language
    if source_language != 'English':
        response = openai.Completion.create(
            prompt=generate_language_translation_prompt(source_language, prompt),
            **const.LANGUAGE_MODEL_PARAMS
        )
        prompt = response["choices"][0]["text"]

        # Double check for abusive content after translation
        content_check(prompt)
        print("HERE 2")

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

def content_check(prompt):
    response = openai.Moderation.create(input=prompt)
    if response["results"][0]["flagged"]:
        raise IllegalContentError(response_obj=response)


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
