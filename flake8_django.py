import ast

from issues import DJ01, DJ02, DJ03, DJ04, DJ05


__version__ = '0.0.1'

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

    def capture_field_issues(self, node, call):
        if not(call in NOT_NULL_TRUE_FIELDS or call in NOT_BLANK_TRUE_FIELDS):
            return

        for keyword in node.keywords:
            if call in NOT_NULL_TRUE_FIELDS and keyword.arg == 'null' and keyword.value.value is True:
                self.issues.append(
                    DJ01(
                        lineno=node.lineno,
                        col=node.col_offset,
                        parameters={'field': call}
                    )
                )
            if call in NOT_BLANK_TRUE_FIELDS and keyword.arg == 'blank' and keyword.value.value is True:
                self.issues.append(
                    DJ02(
                        lineno=node.lineno,
                        col=node.col_offset,
                        parameters={'field': call}
                    )
                )

    def capture_url_issues(self, node):
        for keyword in node.keywords:
            if keyword.arg == 'name' and '-' in keyword.value.s:
                self.issues.append(
                    DJ03(
                        lineno=node.lineno,
                        col=node.col_offset,
                        parameters={}
                    )
                )
                return

    def capture_url_missing_namespace(self, node):
        """
        Capture missing namespace in url include.
        """
        has_include = False
        found_namespace = False

        for arg in node.args:
            if not(isinstance(arg, ast.Call) and isinstance(arg.func, ast.Name)):
                continue
            if arg.func.id == 'include':
                has_include = True
                for keyword in arg.keywords:
                    if keyword.arg == 'namespace':
                        found_namespace = True
                        return

        if has_include and not found_namespace:
            self.issues.append(
                DJ05(
                    lineno=node.lineno,
                    col=node.col_offset,
                    parameters={}
                )
            )

    def capture_use_of_locals(self, node):
        """
        Captures the use of locals() in render function.
        """
        for arg in node.args:
            if isinstance(arg, ast.Call) and arg.func.id == 'locals':
                self.issues.append(
                    DJ04(
                        lineno=node.lineno,
                        col=node.col_offset,
                        parameters={}
                    )
                )

    def get_call_name(self, node):
        call = ''
        if isinstance(node.func, ast.Attribute):
            call = node.func.attr
        elif isinstance(node.func, ast.Name):
            call = node.func.id
        return call

    def visit_Call(self, node):
        """
        blank=True is not recommended to be used in fields specified in NOT_BLANK_TRUE_FIELDS.

        null=True is not recommended to be used in fields specified in NOT_NULL_TRUE_FIELDS
        """
        call = self.get_call_name(node)
        
        if call == 'url':
            self.capture_url_issues(node)
            self.capture_url_missing_namespace(node)

        if call == 'render':
            self.capture_use_of_locals(node)

        self.capture_field_issues(node, call)


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
