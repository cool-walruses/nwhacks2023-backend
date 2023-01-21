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

CODEX_MODEL = "code-davinci-002" 
MAX_TOKENS = 1024
TEMPERATURE = 0.6

LANG_COMMENTS = {
    "python" : CommentWrapper('"""', '"""'),
    "java" : CommentWrapper('/*', '*/'),
    "javascript" : CommentWrapper('/*', '*/'),
    "c" : CommentWrapper('/*', '*/'),
    "c++" : CommentWrapper('/*', '*/'),
    "c#" : CommentWrapper('/*', '*/'),
    "golang" : CommentWrapper('/*', '*/'),
    "php" : CommentWrapper('/*', '*/'),
    "mysql" : CommentWrapper('/*', '*/'),
    "html" : CommentWrapper('<!--', '-->'),
    "css" : CommentWrapper('/*', '*/'),
    "react" : CommentWrapper('/*', '*/')
}

