# flake8-django

[![pypi](https://img.shields.io/pypi/v/flake8-django.svg)](https://pypi.python.org/pypi/flake8-django/)
![CI](https://github.com/rocioar/flake8-django/workflows/CI/badge.svg)[![Codecov](https://codecov.io/gh/rocioar/flake8-django/branch/master/graph/badge.svg)](https://codecov.io/gh/rocioar/flake8-django)
[![Downloads](https://pepy.tech/badge/flake8-django)](https://pepy.tech/project/flake8-django)

A flake8 plugin to detect bad practices on Django projects.

## Installation

Install from pip with:

```
$ pip install flake8-django
```

## Testing

flake8-django uses pytest for tests. To run them use:

```
$ pytest
````

Run coverage report using:

```
$ pytest --cov=.
```

## List of warnings

| Warning | Description |
| --- | --- |
| [`DJ01`]((https://github.com/rocioar/flake8-django/wiki/%5BDJ01%5D-Avoid-using-null=True-on-string-based-fields-such-as-CharField-and-TextField)) | Avoid using null=True on string-based fields such as CharField and TextField |
| [`DJ03`]((https://github.com/rocioar/flake8-django/wiki/%5BDJ03%5D-Avoid-passing-locals()-as-context-to-a-render-function)) | Avoid passing locals() as context to a render function |
| [`DJ06`]((https://github.com/rocioar/flake8-django/wiki/%5BDJ06%5D-Do-not-use-exclude-with-ModelForm,-use-fields-instead)) | Do not use exclude with ModelForm, use fields instead |
| [`DJ07`]((https://github.com/rocioar/flake8-django/wiki/%5BDJ07%5D-Do-not-set-fields-to-'__all__'-on-ModelForm,-use-fields-instead)) | Do not use __all__ with ModelForm, use fields instead |
| [`DJ08`]((https://github.com/rocioar/flake8-django/wiki/%5BDJ08%5D-Model-does-not-define-__str__-method)) | Model does not define __str__ method |
| [`DJ12`]((https://github.com/rocioar/flake8-django/wiki/%5BDJ12%5D-Order-of-Model's-inner-classes,-methods,-and-fields-does-not-follow-the-Django-Style-Guide)) | Order of Model's inner classes, methods, and fields does not follow the [Django Style Guide](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#model-style) |

## Licence

GPL

## Thanks

[@stummjr](https://github.com/stummjr) for teaching me AST, and what I could do with it. His [blog](https://stummjr.org/post/building-a-custom-flake8-plugin/) is cool.
