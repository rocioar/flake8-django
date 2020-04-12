import pytest

from .utils import run_check, error_code_in_result


def test_render_doesnt_use_locals_fails():
    code = "render(request, 'template.html', locals())"
    result = run_check(code)
    assert error_code_in_result('DJ03', result)


@pytest.mark.parametrize('code', [
    "render(request, 'template.html', {'test': 'test'})",
    "return render(request, 'template.html', self.get_context_data())",
])
def test_render_doesnt_use_locals_success(code):
    result = run_check(code)
    assert not error_code_in_result('DJ03', result)
