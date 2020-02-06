from .utils import run_check, load_fixture_file, error_code_in_result


def test_model_form_doesnt_set_exclude_fails():
    code = load_fixture_file('model_form_exclude.py')
    result = run_check(code)
    assert error_code_in_result('DJ06', result)


def test_model_form_doesnt_set_exclude_success():
    code = load_fixture_file('model_form_fields.py')
    result = run_check(code)
    assert len(result) == 0
    assert not error_code_in_result('DJ06', result)


def test_model_form_doesnt_set_fields_dunder_all():
    code = load_fixture_file('model_form_fields_all.py')
    result = run_check(code)
    assert error_code_in_result('DJ07', result)
