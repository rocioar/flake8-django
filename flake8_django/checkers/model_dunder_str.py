import ast

from .base_model_checker import BaseModelChecker
from .issue import Issue


class DJ08(Issue):
    code = 'DJ08'
    description = 'Model does not define __str__ method'


class ModelDunderStrMissingChecker(BaseModelChecker):
    model_name_lookup = 'Model'

    def checker_applies(self, node):
        for base in node.bases:
            if self.is_model_name_lookup(base) or self.is_models_name_lookup_attribute(base):
                if not self.is_abstract_model(node):
                    return True
        return False

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
