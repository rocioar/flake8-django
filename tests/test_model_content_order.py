from .utils import run_check, load_fixture_file


def test_model_content_order_succeeds():
    code = load_fixture_file('model_content_order.py')
    issues = list(map(lambda x: x[2], run_check(code)))
    assert len(issues) == 3
    assert 'DJ09' in issues[0] and 'before __str__' in issues[0]
    assert 'DJ09' in issues[1] and 'before manager' in issues[1]
    assert 'DJ09' in issues[2] and 'before custom method' in issues[2]
