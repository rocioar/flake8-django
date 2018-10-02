import ast

from checkers import ModelFieldChecker, URLChecker, RenderChecker

__version__ = '0.0.2'


class DjangoStyleFinder(ast.NodeVisitor):
    """
    Visit the node, and return issues.
    """
    checkers = [
        ModelFieldChecker(),
        URLChecker(),
        RenderChecker(),
    ]

    def __init__(self, *args, **kwargs):
        super(DjangoStyleFinder, self).__init__(*args, **kwargs)
        self.issues = []

    def visit_Call(self, node):
        for checker in self.checkers:
            issues = checker.run(node)
            if issues:
                self.issues.extend(issues)


class DjangoStyleChecker(object):
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

        for issue in parser.issues:
            yield (issue.lineno, issue.col, issue.message, DjangoStyleChecker)
