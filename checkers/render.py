import ast

from .checker import Checker
from .issue import Issue


class DJ04(Issue):
    code = 'DJ04'
    description = 'Use of locals() is not recommended in render function, use explicit arguments'


class RenderChecker(Checker):

    def run(self, node):
        """
        Captures the use of locals() in render function.
        """
        if self.get_call_name(node) != 'render':
            return
        issues = []
        for arg in node.args:
            if isinstance(arg, ast.Call) and arg.func.id == 'locals':
                issues.append(
                    DJ04(
                        lineno=node.lineno,
                        col=node.col_offset,
                    )
                )
        return issues
