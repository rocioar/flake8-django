import ast

from .checker import Checker
from .issue import Issue


class DJ13(Issue):
    code = 'DJ13'
    description = '@receiver decorator must be on top of all the other decorators'


class DecoratorChecker(Checker):
    def run(self, node):
        issues = []
        seen_receiver = False
        for pos, decorator in enumerate(node.decorator_list):
            name = (
                decorator.func.id if isinstance(decorator, ast.Call)
                else decorator.id
            )

            if name == 'receiver' and pos > 0 and not seen_receiver:
                issues.append(DJ13(lineno=node.lineno, col=node.col_offset))

            if name != 'receiver' and seen_receiver:
                seen_receiver = False
            elif name == 'receiver':
                seen_receiver = True

        return issues
