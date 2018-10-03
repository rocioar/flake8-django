import ast
import os

from flake8_django import DjangoStyleChecker


def run_check(code):
    tree = ast.parse(code)
    checker = DjangoStyleChecker(tree, None)
    return list(checker.run())


def load_fixture_file(filename):
    path = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        filename
    )
    return open(path).read()
