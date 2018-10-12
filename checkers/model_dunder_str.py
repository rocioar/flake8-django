import ast

from .checker import Checker
from .issue import Issue


class DJ08(Issue):
    code = 'DJ08'
    description = '__str__ method should be present in all db models'


class ModelDunderStrMissingChecker(Checker):

    def checker_applies(self, node):
        for base in node.bases:
            if self.is_model_name(base) or self.is_models_attribute(base):
                return True
        return False

    def is_model_name(self, base):
        return (
            isinstance(base, ast.Name) and
            base.id == 'Model'
        )

    def is_models_attribute(self, base):
        return (
            isinstance(base, ast.Attribute) and
            isinstance(base.value, ast.Name) and
            base.value.id == 'models' and base.attr == 'Model'
        )

    def is_dunder_str_method(self, element):
        return (
            isinstance(element, ast.FunctionDef) and
            element.name == '__str__'
        )

    def run(self, node):
        if not self.checker_applies(node):
            return

        if not any(self.is_dunder_str_method(elem) for elem in node.body):
            return [
                DJ08(
                    lineno=node.lineno,
                    col=node.col_offset
                )
            ]

        return []
