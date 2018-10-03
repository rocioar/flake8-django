from .utils import run_check, load_fixture_file


def test_render_doesnt_use_locals_fails():
    code = load_fixture_file('model_form_exclude.py')
    assert len(run_check(code)) == 3
    assert 'DJ06' in run_check(code)[0][2]
    assert 'DJ06' in run_check(code)[1][2]
    assert 'DJ07' in run_check(code)[2][2]


def test_render_doesnt_use_locals_success():
    code = load_fixture_file('model_form_fields.py')
    assert len(run_check(code)) == 0
