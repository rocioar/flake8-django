from .utils import run_check, load_fixture_file


def test_model_without_dunder_str_method_fails():
    code = load_fixture_file('model_without_dunder_str.py')
    assert len(run_check(code)) == 2
    assert 'DJ08' in run_check(code)[0][2]
    assert 'DJ08' in run_check(code)[1][2]


def test_model_with_dunder_str_method_success():
    code = load_fixture_file('model_dunder_str.py')
    assert len(run_check(code)) == 0
