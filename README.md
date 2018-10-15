# flake8-django

[![CircleCI](https://circleci.com/gh/rocioar/flake8-django/tree/master.svg?style=shield)](https://circleci.com/gh/rocioar/flake8-django/tree/master)
[![Codecov](https://codecov.io/gh/rocioar/flake8-django/branch/master/graph/badge.svg)](https://codecov.io/gh/rocioar/flake8-django)
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
| `DJ02` | Using `blank=True` is not recommended on `BooleanField`|
| `DJ03` | Using locals() in render function is not recommended, use explicit arguments |
| `DJ04` | Using dashes in url names is discouraged, use underscores instead |
| `DJ05` | URLs include() should set a namespace |
| `DJ06` | ModelForm should not set exclude, instead it should use fields, which is an explicit list of all the fields that should be included in the form |
| `DJ07` | ModelForm.Meta should not set fields to `__all__`|
| `DJ08` | Models that inherits from django db models should set `__str__`|

## Licence

GPL

## Thanks

[@stummjr](https://github.com/stummjr) for teaching me AST, and what I could do with it. His [blog](https://dunderdoc.wordpress.com/) is cool.
