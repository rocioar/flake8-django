from .utils import run_check


def test_render_doesnt_use_locals_fails():
    code = "render(request, 'template.html', locals())"
    assert len(run_check(code)) == 1
    assert 'DJ03' in run_check(code)[0][2]


def test_render_doesnt_use_locals_success():
    code = "render(request, 'template.html', {'test': 'test'})"
    assert len(run_check(code)) == 0
