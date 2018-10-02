import ast

from flake8_django import DjangoStyleChecker


def run_check(code):
    tree = ast.parse(code)
    checker = DjangoStyleChecker(tree, None)
    return list(checker.run())
