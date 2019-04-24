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


def error_code_in_result(error_code, result):
    """
    assert that a specific error_code is into the results

    :param error_code:
    :param result:
    :return:
    """
    for element in result:
        if error_code in element[2]:
            return True
    return False
