import ast

import pytest

from flake8_django import DjangoStyleChecker, NOT_BLANK_TRUE_FIELDS, NOT_NULL_TRUE_FIELDS


def run_check(code):
    tree = ast.parse(code)
    checker = DjangoStyleChecker(tree, None)
    return list(checker.run())


@pytest.mark.parametrize('field_type', NOT_NULL_TRUE_FIELDS)
def test_not_null_fields(field_type):
    code = "field = models.{}(null=True)".format(field_type)
    assert len(run_check(code)) == 1


@pytest.mark.parametrize('field_type', NOT_BLANK_TRUE_FIELDS)
def test_not_blank_fields(field_type):
    code = "another_field = models.{}(blank=True)".format(field_type)
    assert len(run_check(code)) == 1


def test_booleanfield_blank_and_null():
    code = "field = models.BooleanField(blank=True, null=True)"
    assert len(run_check(code)) == 2


def test_url_name_with_dash():
    code = "url(name='test-1')"
    assert len(run_check(code) == 1)