import pytest

from .utils import run_check


@pytest.mark.parametrize('code', [
    "url(name='test-1')",
    "path(name='test-1')",
    "re_path(name='test-1')",
])
def test_url_name_with_dash_fails(code):
    assert len(run_check(code)) == 1
    assert 'DJ04' in run_check(code)[0][2]


@pytest.mark.parametrize('code', [
    "url('/test/', View.as_view(), name='test_1')",
    "path('/test/', View.as_view(), name='test_1')",
    "re_path('/test/', View.as_view(), name='test_1')",
])
def test_url_name_with_underscore_sucess(code):
    assert len(run_check(code)) == 0


@pytest.mark.parametrize('code', [
    "url('/test/', include())",
    "path('/test/', include())",
    "re_path('/test/', include())"
])
def test_url_include_without_namespace_fails(code):
    assert len(run_check(code)) == 1
    assert 'DJ05' in run_check(code)[0][2]


@pytest.mark.parametrize('code', [
    "url('/test/', include('test', namespace='test'))",
    "url('/test/', includes('test2', namespace='test-2'))",
    "path('/test/', include('test', namespace='test'))",
    "path('/test/', includes('test2', namespace='test-2'))",
    "re_path('/test/', include('test', namespace='test'))",
    "re_path('/test/', includes('test2', namespace='test-2'))",
])
def test_url_include_with_namespace_success(code):
    assert len(run_check(code)) == 0
