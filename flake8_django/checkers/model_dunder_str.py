import astroid

from .base_model_checker import BaseModelChecker
from .issue import Issue


class DJ08(Issue):
    code = 'DJ08'
    description = 'Model does not define __str__ method'


class ModelDunderStrMissingChecker(BaseModelChecker):
    model_name_lookups = ['.Model', 'django.db.models.base.Model']

    def checker_applies(self, node):
        return self.is_model(node) and not self.is_abstract_model(node)

    def is_dunder_str_method(self, element):
        return (
            isinstance(element, astroid.FunctionDef) and
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
