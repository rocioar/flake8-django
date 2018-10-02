# flake8-django

[![CircleCI](https://circleci.com/gh/rocioar/flake8-django/tree/master.svg?style=svg)](https://circleci.com/gh/rocioar/flake8-django/tree/master)

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
| `DJ01` | Using `null=True` is not recommended for some of the Django ORM fields. E.g. `CharField`, `EmailField`, `ImageField`, `FileField`, `BooleanField`, `UUIDField`, `SlugField`, `TextField` |
| `DJ02` | Using `blank=True` is not recommended on `BooleanField`, use `NullBooleanField` instead |
| `DJ03` | Using locals() in render function is not recommended, use explicit arguments |
| `DJ04` | Using dashes in url names is discouraged, use underscores instead |
| `DJ05` | URLs include() should set a namespace |

## Licence

GPL

## Thanks

[@stummjr](https://github.com/stummjr) for teaching me AST, and what I could do with it. His [blog](https://dunderdoc.wordpress.com/) is cool.
