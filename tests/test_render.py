from .utils import run_check, error_code_in_result


def test_render_doesnt_use_locals_fails():
    code = "render(request, 'template.html', locals())"
    result = run_check(code)
    assert error_code_in_result('DJ03', result)


def test_render_doesnt_use_locals_success():
    code = "render(request, 'template.html', {'test': 'test'})"
    result = run_check(code)
    assert not error_code_in_result('DJ03', result)
