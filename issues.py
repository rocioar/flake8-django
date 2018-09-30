"""
Defines all issues that can be captured by the linter.
"""
from collections import namedtuple
from functools import partial


Issue = namedtuple('Issue', ['code', 'lineno', 'col', 'message', 'parameters'])

DJ01 = partial(
    Issue,
    code='DJ01',
    message='{code} null=True not recommended to be used in {field}'
)
DJ02 = partial(
    Issue,
    code='DJ02',
    message='{code} blank=True not recommended to be used in {field} use NullBooleanField instead'
)
DJ03 = partial(
    Issue,
    code='DJ03',
    message='{code} not recommended to use dashes in url name, use underscore instead'
)
DJ04 = partial(
    Issue,
    code='DJ04',
    message='{code} Use of locals() is not recommended in render function, use explicit arguments'
)
DJ05 = partial(
    Issue,
    code='DJ05',
    message='{code} Missing namespace in urls include()'
)
