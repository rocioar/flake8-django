import pytest

from checkers.model_fields import NOT_BLANK_TRUE_FIELDS, NOT_NULL_TRUE_FIELDS

from .utils import run_check


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
