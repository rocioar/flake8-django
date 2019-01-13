import ast

from .checker import Checker


class BaseModelChecker(Checker):
    """
    Base class for checkers that must lookup for Model like nodes.
    """

    model_name_lookup = None

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
