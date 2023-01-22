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
    'model' : 'code-davinci-002',
    'temperature' : 0.6,
    'max_tokens' : 1024
}

LANGUAGE_MODEL_PARAMS = {
    'model' : 'text-davinci-003',
    'temperature' : 0.6,
    'max_tokens' : 1024
}

ENGLISH_TO_ORIGINAL_LANGUAGE_MODEL_PARAMS = {
    'model' : 'text-davinci-003',
    'temperature' : 0,
    'max_tokens' : 1024
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
