import ast

import pytest

from flake8_django import DjangoStyleChecker
from checkers.model_fields import NOT_BLANK_TRUE_FIELDS, NOT_NULL_TRUE_FIELDS


def run_check(code):
    tree = ast.parse(code)
    checker = DjangoStyleChecker(tree, None)
    return list(checker.run())


@pytest.mark.parametrize('field_type', NOT_NULL_TRUE_FIELDS)
def test_not_null_fields_fails(field_type):
    code = "field = models.{}(null=True)".format(field_type)
    assert len(run_check(code)) == 1
    assert 'DJ01' in run_check(code)[0][2]


@pytest.mark.parametrize('field_type', NOT_NULL_TRUE_FIELDS)
def test_not_null_fields_success(field_type):
    code = "field = models.{}()".format(field_type)
    assert len(run_check(code)) == 0


@pytest.mark.parametrize('field_type', NOT_BLANK_TRUE_FIELDS)
def test_not_blank_fields_fails(field_type):
    code = "another_field = models.{}(blank=True)".format(field_type)
    assert len(run_check(code)) == 1
    assert 'DJ02' in run_check(code)[0][2]


@pytest.mark.parametrize('field_type', NOT_BLANK_TRUE_FIELDS)
def test_not_blank_fields_sucess(field_type):
    code = "another_field = models.{}()".format(field_type)
    assert len(run_check(code)) == 0


def test_booleanfield_blank_and_null_fails():
    code = "field = models.BooleanField(blank=True, null=True)"
    assert len(run_check(code)) == 2
    assert 'DJ01' in run_check(code)[1][2]
    assert 'DJ02' in run_check(code)[0][2]


def test_url_name_with_dash_fails():
    code = "url(name='test-1')"
    assert len(run_check(code)) == 1
    assert 'DJ03' in run_check(code)[0][2]


def test_url_name_with_dash_sucess():
    code = "url('/test/', View.as_view(), name='test_1')"
    assert len(run_check(code)) == 0


def test_render_doesnt_use_locals_fails():
    code = "render(request, 'template.html', locals())"
    assert len(run_check(code)) == 1
    assert 'DJ04' in run_check(code)[0][2]


def test_render_doesnt_use_locals_success():
    code = "render(request, 'template.html', {'test': 'test'})"
    assert len(run_check(code)) == 0


def test_url_include_without_namespace_fails():
    code = "url('/test/', View.as_view(), include())"
    assert len(run_check(code)) == 1
    assert 'DJ05' in run_check(code)[0][2]


def test_url_include_with_namespace_success():
    code = "url('/test/', include(namespace='test'))"
    assert len(run_check(code)) == 0
