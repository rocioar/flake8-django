from .utils import run_check, load_fixture_file


def test_model_content_order_succeeds():
    code = load_fixture_file('model_content_order.py')
    issues = run_check(code)
    assert len(issues) == 3
    assert 'DJ12' in issues[0][2]
    assert 'before Meta class' in issues[0][2]
    assert 'DJ12' in issues[1][2]
    assert 'before manager' in issues[1][2]
    assert 'DJ12' in issues[2][2]
    assert 'before custom method' in issues[2][2]
