import ast

import django

from .checker import Checker
from .issue import Issue


class DJ09(Issue):
    code = 'DJ09'
    description = 'New applications should avoid default_app_config'


class DefaultAppConfigChecker(Checker):

    def run(self, node):
        if django.VERSION < (1, 7):
            return []
        issues = []
        for elem in node.body:
            if not isinstance(elem, ast.Assign):
                continue
            target_names = map(lambda n: n.id == 'default_app_config', elem.targets)
            if any(target_names):
                issues.append(DJ09(
                    elem.lineno,
                    elem.col_offset,
                ))
        return issues
