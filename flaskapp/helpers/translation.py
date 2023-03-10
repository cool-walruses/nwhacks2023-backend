import openai
import flaskapp.helpers.constants as const
from flaskapp.helpers.exceptions import IllegalContentError, IllegalResponseError


def generate_response(programming_language, prompt):
    too_long_boolean = True
    MAXRUN = 3
    currentRun = 0

    # Check for abusive content
    content_check(prompt)

    # Detect the language in the prompt
    response = openai.Completion.create(
        prompt=generate_language_detection_prompt(prompt),
        **const.LANGUAGE_MODEL_PARAMS
    )
    source_language = response["choices"][0]["text"].strip().title()

    # Translate from source language
    if source_language != 'English':
        response = openai.Completion.create(
            prompt=generate_language_translation_prompt(source_language, prompt),
            **const.LANGUAGE_MODEL_PARAMS
        )
        prompt = response["choices"][0]["text"].strip()

        # Double check for abusive content after translation
        content_check(prompt)

    # Make request to openai API
    current_text = ""
    while currentRun < MAXRUN:
        response = openai.Completion.create(
            prompt=generate_code_prompt(programming_language, prompt),
            **const.CODEX_MODEL_PARAMS
        )
        if response["choices"][0]["finish_reason"] == "stop":
            current_text = response["choices"][0]["text"]
            too_long_boolean = False
            break
        currentRun = currentRun + 1

    if too_long_boolean:
        raise IllegalResponseError()

    # Translate back to original language if needed
    if source_language != 'English':
        response = openai.Completion.create(
            prompt=generate_code_language_translation_prompt(source_language, current_text + "\n"),
            **const.ENGLISH_TO_ORIGINAL_LANGUAGE_MODEL_PARAMS
        )
        current_text = response["choices"][0]["text"]

    return current_text

def content_check(prompt):
    response = openai.Moderation.create(input=prompt)
    if response["results"][0]["flagged"]:
        raise IllegalContentError(response_obj=response)

def generate_language_detection_prompt(prompt):
    return "\n".join([
        f"What language is the following text in:",
        f"{prompt}"
    ])

def generate_language_translation_prompt(source_language, prompt):
    return "\n".join([
        f"Translate the following from {source_language} to English:",
        f"{prompt}"
    ])

def generate_code_language_translation_prompt(source_language, prompt):
    return "\n".join([
        f"Keep the code in English, but translate the comments and variables into {source_language}:\n",
        f"{prompt}"
    ])

def generate_code_prompt(programming_language, prompt):
    return "\n".join([
            const.LANG_COMMENTS[programming_language].startToken,
            f"In {programming_language}, {prompt}",
            const.LANG_COMMENTS[programming_language].endToken
        ])
