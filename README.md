# flake8-django

[![pypi](https://img.shields.io/pypi/v/flake8-django.svg)](https://pypi.python.org/pypi/flake8-django/)
![CI](https://github.com/rocioar/flake8-django/workflows/CI/badge.svg)[![Codecov](https://codecov.io/gh/rocioar/flake8-django/branch/master/graph/badge.svg)](https://codecov.io/gh/rocioar/flake8-django)
[![Downloads](https://pepy.tech/badge/flake8-django)](https://pepy.tech/project/flake8-django)

A flake8 plugin for Django projects.

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
| `DJ01` | Using `null=True` is not recommended for some of the Django ORM fields. E.g. `CharField`, `EmailField`, `ImageField`, `FileField`, `UUIDField`, `SlugField`, `TextField` |
| `DJ03` | Using locals() in render function is not recommended, use explicit arguments |
| `DJ06` | ModelForm should not set exclude, instead it should use fields, which is an explicit list of all the fields that should be included in the form |
| `DJ07` | ModelForm.Meta should not set fields to `__all__`|
| `DJ08` | Models that inherits from django db models should set `__str__`|
| `DJ12` | Order of model inner classes and standard methods does not follow [Django style guide](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#model-style) |

## Licence

GPL

## Thanks

[@stummjr](https://github.com/stummjr) for teaching me AST, and what I could do with it. His [blog](https://stummjr.org/post/building-a-custom-flake8-plugin/) is cool.
