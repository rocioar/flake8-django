import django

from .utils import run_check, load_fixture_file


def test_default_app_config_django_16(monkeypatch):
    monkeypatch.setattr(django, 'VERSION', (1, 6))
    code = load_fixture_file('default_app_config.py')
    assert len(run_check(code)) == 0


def test_default_app_config_django_17(monkeypatch):
    monkeypatch.setattr(django, 'VERSION', (1, 7))
    code = load_fixture_file('default_app_config.py')
    assert len(run_check(code)) == 1
    assert 'DJ09' in run_check(code)[0][2]
