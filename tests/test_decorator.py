import pytest

from .utils import run_check, error_code_in_result


def test_receiver_non_continuous():
    code = """\
@receiver(post_delete, sender=User)
@cached
@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    pass"""

    result = run_check(code)
    assert error_code_in_result('DJ13', result)


def test_single_receiver_decorator():
    code = """\
@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    pass"""

    result = run_check(code)
    assert not error_code_in_result('DJ03', result)


def test_wrong_order():
    code = """\
@atomic
@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
   pass"""

    result = run_check(code)
    assert error_code_in_result('DJ13', result)
