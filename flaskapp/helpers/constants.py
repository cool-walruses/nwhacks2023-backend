class CommentWrapper:

    def __init__(self, startToken, endToken):
        self.__startToken = startToken
        self.__endToken = endToken

    @property
    def startToken(self):
        return self.__startToken

    @property
    def endToken(self):
        return self.__endToken

CODEX_MODEL_PARAMS = {
    'model' : 'code-cushman-001',
    'temperature' : 0.2,
    'max_tokens' : 1900,
    'n' : 6
}

LANGUAGE_MODEL_PARAMS = {
    'model' : 'text-davinci-003',
    'temperature' : 0.6,
    'max_tokens' : 1024,
}

ENGLISH_TO_ORIGINAL_LANGUAGE_MODEL_PARAMS = {
    'model' : 'text-davinci-003',
    'temperature' : 0,
    'max_tokens' : 2047,
    'frequency_penalty' : 0.1
}

LANG_COMMENTS = {
    "Python" : CommentWrapper('"""', '"""'),
    "Java" : CommentWrapper('/*', '*/'),
    "Javascript" : CommentWrapper('/*', '*/'),
    "C" : CommentWrapper('/*', '*/'),
    "C++" : CommentWrapper('/*', '*/'),
    "C#" : CommentWrapper('/*', '*/'),
    "Golang" : CommentWrapper('/*', '*/'),
    "Php" : CommentWrapper('/*', '*/'),
    "Html" : CommentWrapper('<!--', '-->'),
    "Css" : CommentWrapper('/*', '*/')
}
