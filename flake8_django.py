import ast

__version__ = '0.1'


NOT_NULL_TRUE_FIELDS = [
    'CharField', 'TextField', 'SlugField', 'EmailField',
    'CommaSeparatedInteger', 'Field', 'UUIDField', 'ImageField',
    'FileField', 'BooleanField'
]

NOT_BLANK_TRUE_FIELDS = ['BooleanField']


class DjangoStyleFinder(ast.NodeVisitor):
    """
    """
    DJ01 = 'DJ01 null=True not recommended to be used in {}'
    DJ02 = 'DJ02 blank=True not recommended to be used in {}'

    def __init__(self, *args, **kwargs):
        super(DjangoStyleFinder, self).__init__(*args, **kwargs)
        self.issues = []

    def visit_Call(self, node):
        """
        blank=True is not recommended to be used in BooleanField.

        null=True is not recommended to be used in CharField, TextField, SlugField,
        EmailField, CommaSeparatedInteger, Field, UUIDField, ImageField, FileField,
        BooleanField.
        """
        if not(isinstance(node.func, ast.Attribute)):
            return

        call = node.func.attr
        # Check that BooleanField can't have blank=True
        # Check that CharField, ImageField, BooleanField, and FileField can't have null=True
        if not(call in NOT_NULL_TRUE_FIELDS or call in NOT_BLANK_TRUE_FIELDS):
            return

        for keyword in node.keywords:
            if keyword.arg == 'null' and keyword.value.id == 'True' and call in NOT_NULL_TRUE_FIELDS:
                issue = ((node.lineno, node.col_offset), self.DJ01.format(call))
                self.issues.append(issue)
            if keyword.arg == 'blank' and keyword.value.id == 'True' and call in NOT_BLANK_TRUE_FIELDS:
                issue = ((node.lineno, node.col_offset), self.DJ02.format(call))
                self.issues.append(issue)


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

        for (lineno, col), message in parser.issues:
            yield (lineno, col, message, DjangoStyleChecker)
