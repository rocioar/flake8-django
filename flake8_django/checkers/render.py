import ast

from .checker import Checker
from .issue import Issue


class DJ03(Issue):
    code = 'DJ03'
    description = 'Avoid passing locals() as context to a render function'


class RenderChecker(Checker):

    def run(self, node):
        """
        Captures the use of locals() in render function.
        """
        if self.get_call_name(node) != 'render':
            return
        issues = []
        for arg in node.args:
            if isinstance(arg, ast.Call) and getattr(arg.func, 'id', '') == 'locals':
                issues.append(
                    DJ03(
                        lineno=node.lineno,
                        col=node.col_offset,
                    )
                )
        return issues
