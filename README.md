# flake8-django

A flake8 plugin for Django projects.

## Installation

To be added

## List of warnings

| Warning | Description |
| --- | --- |
| `DJ01` | Using `null=True` is not recommended for some of the Django ORM fields. E.g. `CharField`, `EmailField`, `ImageField`, `FileField`, `BooleanField`, `UUIDField`, `SlugField`, `TextField` |
| `DJ02` | Using `blank=True` is not recommended on `BooleanField`, use `NullBooleanField` instead |
| `DJ03` | Using dashes in url names is discouraged, use underscores instead |

## Licence

GPL
