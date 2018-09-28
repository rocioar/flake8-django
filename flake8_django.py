import ast

from issues import DJ01, DJ02


__version__ = '0.1'

NOT_NULL_TRUE_FIELDS = [
    'CharField', 'TextField', 'SlugField', 'EmailField', 'Field',
    'UUIDField', 'ImageField', 'FileField', 'BooleanField'
]

NOT_BLANK_TRUE_FIELDS = ['BooleanField']


class DjangoStyleFinder(ast.NodeVisitor):
    """
    Visit the node, and return issues.
    """

    def __init__(self, *args, **kwargs):
        super(DjangoStyleFinder, self).__init__(*args, **kwargs)
        self.issues = []

    def visit_Call(self, node):
        """
        blank=True is not recommended to be used in fields specified in NOT_BLANK_TRUE_FIELDS.

        null=True is not recommended to be used in fields specified in NOT_NULL_TRUE_FIELDS
        """
        if not(isinstance(node.func, ast.Attribute)):
            return

        call = node.func.attr
        if not(call in NOT_NULL_TRUE_FIELDS or call in NOT_BLANK_TRUE_FIELDS):
            return

        for keyword in node.keywords:
            if keyword.arg == 'null' and keyword.value.id == 'True' and call in NOT_NULL_TRUE_FIELDS:
                self.issues.append(
                    DJ01(
                        lineno=node.lineno,
                        col=node.col_offset,
                        parameters={'field': call}
                    )
                )
            if keyword.arg == 'blank' and keyword.value.id == 'True' and call in NOT_BLANK_TRUE_FIELDS:
                self.issues.append(
                    DJ02(
                        lineno=node.lineno,
                        col=node.col_offset,
                        parameters={'field': call}
                    )
                )


class DjangoStyleChecker():
    """
    Check common Django Style errors
    """
    options = None
    name = 'flake8-django'
    version = __version__

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    def run(self):
        parser = DjangoStyleFinder()
        parser.visit(self.tree)

        for code, lineno, col, message, parameters in parser.issues:
            yield (lineno, col, message.format(code=code, **parameters), DjangoStyleChecker)
