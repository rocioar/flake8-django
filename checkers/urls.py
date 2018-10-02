import ast

from .checker import Checker
from .issue import Issue


class DJ03(Issue):
    code = 'DJ03'
    description = 'not recommended to use dashes in url name, use underscore instead'


class DJ05(Issue):
    code = 'DJ05'
    description = 'Missing namespace in urls include()'


class URLChecker(Checker):

    def run(self, node):
        if self.get_call_name(node) != 'url':
            return
        issues = []
        self.capture_url_issues(node, issues)
        self.capture_url_missing_namespace(node, issues)
        return issues

    def capture_url_issues(self, node, issues):
        for keyword in node.keywords:
            if keyword.arg == 'name' and '-' in keyword.value.s:
                return issues.append(
                    DJ03(
                        lineno=node.lineno,
                        col=node.col_offset,
                    )
                )

    def capture_url_missing_namespace(self, node, issues):
        """
        Capture missing namespace in url include.
        """
        has_include = False
        found_namespace = False

        for arg in node.args:
            if not(isinstance(arg, ast.Call) and isinstance(arg.func, ast.Name)):
                continue
            if arg.func.id == 'include':
                has_include = True
                for keyword in arg.keywords:
                    if keyword.arg == 'namespace':
                        found_namespace = True
                        return

        if has_include and not found_namespace:
            return issues.append(
                DJ05(
                    lineno=node.lineno,
                    col=node.col_offset,
                )
            )
