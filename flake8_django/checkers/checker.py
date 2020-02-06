import ast


class Checker(object):
    """
    Abstract class for Checkers.
    """

    @staticmethod
    def get_call_name(node):
        """
        Return call name for the given node.
        """
        if isinstance(node.func, ast.Attribute):
            return node.func.attr
        elif isinstance(node.func, ast.Name):
            return node.func.id

    def run(self, node):
        """
        Method that runs the checks and returns the issues.
        """
        return NotImplementedError  # pragma: no cover
