# flake8-django

[![Build Status](https://travis-ci.com/rocioar/flake8-django.svg?branch=master)](https://travis-ci.com/rocioar/flake8-django)

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

## Thanks

[@stummjr](https://github.com/stummjr) for teaching me AST, and what I could do with it. His [blog](https://dunderdoc.wordpress.com/) is cool.
