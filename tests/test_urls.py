import pytest

from .utils import run_check, error_code_in_result


@pytest.mark.parametrize('code', [
    "url('/test/', include())",
    "path('/test/', include())",
    "re_path('/test/', include())"
])
def test_url_include_without_namespace_fails(code):
    result = run_check(code)
    assert error_code_in_result('DJ05', result)


@pytest.mark.parametrize('code', [
    "url('/test/', include('test', namespace='test'))",
    "url('/test/', includes('test2', namespace='test-2'))",
    "path('/test/', include('test', namespace='test'))",
    "path('/test/', includes('test2', namespace='test-2'))",
    "re_path('/test/', include('test', namespace='test'))",
    "re_path('/test/', includes('test2', namespace='test-2'))",
])
def test_url_include_with_namespace_success(code):
    result = run_check(code)
    assert not error_code_in_result('DJ05', result)
