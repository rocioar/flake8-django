from .utils import run_check, load_fixture_file, error_code_in_result


def test_model_without_dunder_str_method_fails():
    code = load_fixture_file('model_without_dunder_str.py')
    result = run_check(code)
    assert error_code_in_result('DJ08', result)


def test_model_with_dunder_str_method_success():
    code = load_fixture_file('model_dunder_str.py')
    result = run_check(code)
    assert not error_code_in_result('DJ08', result)


def test_abstract_model_without_dunder_str_method_success():
    """
    Abstract models without __str__ succeed.
    """
    code = load_fixture_file('abstract_model_without_dunder_str.py')
    result = run_check(code)
    assert not error_code_in_result('DJ08', result)


def test_abstract_model_with_dunder_str_method_success():
    """
    Abstract models with __str__ succeed.
    """
    code = load_fixture_file('abstract_model_dunder_str.py')
    result = run_check(code)
    assert not error_code_in_result('DJ08', result)


def test_model_dunder_str_inherited_from_abstract_model():
    """
    A concrete model with an inherited __str__ method from an sbstract model succeeds.
    """
    code = load_fixture_file('model_dunder_str_inherited_from_abstract_model.py')
    result = run_check(code)

    assert not error_code_in_result('DJ08', result)
