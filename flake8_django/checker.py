import ast

from flake8_django.checkers import (
    DecoratorChecker,
    ModelContentOrderChecker,
    ModelDunderStrMissingChecker,
    ModelFieldChecker,
    ModelFormChecker,
    ModelMetaChecker,
    RenderChecker,
)

__version__ = '1.1.5'


CHECKS_DISABLED_BY_DEFAULT = ['DJ10', 'DJ11']


class DjangoStyleFinder(ast.NodeVisitor):
    """
    Visit the node, and return issues.
    """
    checkers = {
        'Call': [
            ModelFieldChecker(),
            RenderChecker(),
        ],
        'ClassDef': [
            ModelFormChecker(),
            ModelDunderStrMissingChecker(),
            ModelMetaChecker(),
            ModelContentOrderChecker(),
        ],
        'FunctionDef': [
            DecoratorChecker(),
        ]
    }

    def __init__(self, *args, **kwargs):
        super(DjangoStyleFinder, self).__init__(*args, **kwargs)
        self.issues = []

    def capture_issues_visitor(self, visitor, node):
        for checker in self.checkers[visitor]:
            issues = checker.run(node)
            if issues:
                self.issues.extend(issues)
        self.generic_visit(node)

    def visit_Call(self, node):
        self.capture_issues_visitor('Call', node)

    def visit_ClassDef(self, node):
        self.capture_issues_visitor('ClassDef', node)

    def visit_FunctionDef(self, node):
        self.capture_issues_visitor('FunctionDef', node)


class DjangoStyleChecker(object):
    """
    Check common Django Style errors
    """
    name = 'flake8-django'
    version = __version__

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    @staticmethod
    def add_options(optmanager):
        """Informs flake8 to ignore checks by default."""
        optmanager.extend_default_ignore(CHECKS_DISABLED_BY_DEFAULT)

    def run(self):
        parser = DjangoStyleFinder()
        parser.visit(self.tree)

        for issue in parser.issues:
            yield issue.lineno, issue.col, issue.message, DjangoStyleChecker
