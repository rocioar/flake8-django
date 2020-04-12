import ast

from .checker import Checker
from .issue import Issue


class DJ05(Issue):
    code = 'DJ05'
    description = 'Missing namespace in urls include()'


class URLChecker(Checker):
    """
    Checks for bad practices on url definition.
    """
    url_function_names = ['url', 'path', 're_path']

    def __init__(self):
        super(URLChecker, self).__init__()
        self.checks = [self.capture_url_missing_namespace]

    def run(self, node):
        if self.get_call_name(node) not in self.url_function_names:
            return

        issues = []
        for check in self.checks:
            issue = check(node)
            if issue:
                issues.append(issue)
        return issues

    def capture_url_missing_namespace(self, node):
        """
        Capture missing namespace in url include.
        """
        for arg in node.args:
            if not(isinstance(arg, ast.Call) and isinstance(arg.func, ast.Name)):
                continue
            if arg.func.id != 'include':
                continue
            for keyword in arg.keywords:
                if keyword.arg == 'namespace':
                    return

            return DJ05(
                lineno=node.lineno,
                col=node.col_offset,
            )
