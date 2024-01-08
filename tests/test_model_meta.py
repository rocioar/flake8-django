from .utils import run_check, load_fixture_file, error_code_in_result


def test_model_with_meta_without_verbose_name_fails():
    code = load_fixture_file('model_with_meta_without_verbose_name.py')
    result = run_check(code)
    assert error_code_in_result('DJ10', result)
    assert error_code_in_result('DJ11', result)


def test_model_abstract_without_meta_success():
    code = load_fixture_file('model_abstract_with_meta_without_verbose_name.py')
    result = run_check(code)
    assert not error_code_in_result('DJ10', result)
    assert not error_code_in_result('DJ11', result)


def test_model_inherited_from_abstract():
    code = load_fixture_file('model_inherited_from_abstract_model.py')
    result = run_check(code)
    assert error_code_in_result('DJ10', result)
    assert error_code_in_result('DJ11', result)


def test_model_without_meta():
    code = load_fixture_file('model_without_meta.py')
    result = run_check(code)
    assert error_code_in_result('DJ10', result)
    assert error_code_in_result('DJ11', result)


def test_model_inherited_from_abstract_with_verbose_name():
    code = load_fixture_file('model_inherited_from_abstract_model_with_verbose_name.py')
    result = run_check(code)

    assert not error_code_in_result('DJ10', result)
    assert not error_code_in_result('DJ11', result)


def test_model_inherited_from_abstract_and_meta_with_verbose_name():
    code = load_fixture_file('model_inherited_from_abstract_model_with_verbose_name_meta.py')
    result = run_check(code)

    assert not error_code_in_result('DJ10', result)
    assert not error_code_in_result('DJ11', result)
