import ast

from .checker import Checker


class BaseModelChecker(Checker):
    """
    Base class for checkers that must lookup for Model like nodes.
    """

    model_name_lookup = None

    @staticmethod
    def _is_abstract_and_set_to_true(element):
        return (
            isinstance(element, ast.Assign)
            and any(target.id == 'abstract' for target in element.targets if isinstance(target, ast.Name))
            and isinstance(element.value, ast.NameConstant)
            and element.value.value is True
        )

    def is_abstract_model(self, base):
        """
        Return True if AST node has a Meta class with abstract = True.
        """
        # look for "class Meta"
        for element in base.body:
            if isinstance(element, ast.ClassDef) and element.name == 'Meta':
                # look for "abstract = True"
                for inner_element in element.body:
                    if self._is_abstract_and_set_to_true(inner_element):
                        return True
        return False

    def is_model_name_lookup(self, base):
        """
        Return True if class is defined as the respective model name lookup declaration
        """
        return (
            isinstance(base, ast.Name) and
            base.id == self.model_name_lookup
        )

    def is_models_name_lookup_attribute(self, base):
        """
        Return True if class is defined as the respective model name lookup declaration
        """
        return (
            isinstance(base, ast.Attribute) and
            isinstance(base.value, ast.Name) and
            base.value.id == 'models' and base.attr == self.model_name_lookup
        )
