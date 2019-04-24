import pytest

from .utils import run_check, error_code_in_result


@pytest.mark.parametrize('code', [
    "url(name='test-1')",
    "path(name='test-1')",
    "re_path(name='test-1')",
])
def test_url_name_with_dash_fails(code):
    result = run_check(code)
    assert error_code_in_result('DJ04', result)


@pytest.mark.parametrize('code', [
    "url('/test/', View.as_view(), name='test_1')",
    "path('/test/', View.as_view(), name='test_1')",
    "re_path('/test/', View.as_view(), name='test_1')",
])
def test_url_name_with_underscore_sucess(code):
    result = run_check(code)
    assert not error_code_in_result('DJ04', result)


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
