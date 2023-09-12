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
    
    def _abstract_ancestor_has_dunder_str(self, node: astroid.ClassDef):
        for ancestor_node in node.local_attr_ancestors('__str__'):
            if self.is_abstract_model(ancestor_node):
                return any(self.is_dunder_str_method(elem) for elem in ancestor_node.body)

        return False

    def run(self, node):
        if not self.checker_applies(node):
            return

        if (
            not any(self.is_dunder_str_method(elem) for elem in node.body) 
            and not self._abstract_ancestor_has_dunder_str(node)
        ):
            return [
                DJ08(
                    lineno=node.lineno,
                    col=node.col_offset
                )
            ]
