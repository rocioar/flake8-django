import ast
import os
import sys

import astroid

from flake8_django.checkers import (DecoratorChecker, ModelContentOrderChecker,
                                    ModelDunderStrMissingChecker,
                                    ModelFieldChecker, ModelFormChecker,
                                    ModelMetaChecker, RenderChecker)

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

    def visit_FunctionDef(self, node):
        self.capture_issues_visitor('FunctionDef', node)


class AstroidTreeVisitor:
    """
    Go through astroid tree and return issues by specified checkers.
    """
    checkers = {
        "ClassDef": (
            ModelMetaChecker(),
            ModelFormChecker(),
            ModelDunderStrMissingChecker(),
            ModelContentOrderChecker(),
        )
    }

    def __init__(self):
        self.issues = []

    def visit(self, tree):
        for node in tree.body:
            self.issues.extend(
                self.run_checkers(
                    node=node,
                    checker_type=node.__class__.__name__,
                ),
            )

    def run_checkers(self, node, checker_type):
        issues = []
        for checker in self.checkers.get(checker_type, []):
            checker_issues = checker.run(node)
            if checker_issues:
                issues.extend(checker_issues)
        return issues


class DjangoStyleChecker(object):
    """
    Check common Django Style errors
    """
    name = 'flake8-django'
    version = __version__
    astroid_manager = astroid.MANAGER

    def __init__(self, tree, filename, lines=[]):
        self.tree = tree
        self.filename = filename
        self.source_code = ''.join(lines)
        self.build_astroid_tree()

    def build_astroid_tree(self):
        sys.path.append(os.getcwd())
        if not self.filename:
            self.astroid_tree = self.astroid_manager.ast_from_string(
                self.source_code,
            )
        else:
            self.astroid_tree = self.astroid_manager.ast_from_file(  # pragma: no cover
                self.filename,
            )

    @staticmethod
    def add_options(optmanager):
        """Informs flake8 to ignore checks by default."""
        optmanager.extend_default_ignore(CHECKS_DISABLED_BY_DEFAULT)

    def run(self):
        parser = DjangoStyleFinder()
        parser.visit(self.tree)

        astroid_parser = AstroidTreeVisitor()
        astroid_parser.visit(self.astroid_tree)

        for issue in parser.issues + astroid_parser.issues:
            yield issue.lineno, issue.col, issue.message, DjangoStyleChecker
