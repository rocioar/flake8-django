from .utils import run_check, load_fixture_file


def test_model_form_doesnt_set_exclude_fails():
    code = load_fixture_file('model_form_exclude.py')
    assert len(run_check(code)) == 2
    assert 'DJ06' in run_check(code)[0][2]
    assert 'DJ06' in run_check(code)[1][2]


def test_model_form_doesnt_set_exclude_success():
    code = load_fixture_file('model_form_fields.py')
    assert len(run_check(code)) == 0
