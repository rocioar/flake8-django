class Issue(object):
    """
    Abstract class for issues.
    """
    code = ''
    description = ''

    def __init__(self, lineno, col, parameters=None):
        self.parameters = {} if parameters is None else parameters
        self.col = col
        self.lineno = lineno

    @property
    def message(self):
        """
        Return issue message.
        """
        message = self.description.format(**self.parameters)
        return '{code} {message}'.format(code=self.code, message=message)
