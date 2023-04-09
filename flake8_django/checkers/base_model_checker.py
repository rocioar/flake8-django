import astroid

from .checker import AstroidBaseChecker
from .utils import node_is_subclass


class BaseModelChecker(AstroidBaseChecker):
    """
    Base class for checkers that must lookup for Model like nodes.
    """

    def is_model(self, node):
        return node_is_subclass(node, self.model_name_lookups)

    @staticmethod
    def _is_abstract_and_set_to_true(node):
        return (
            isinstance(node, astroid.Assign)
            and any(
                target.name == 'abstract'
                for target in node.targets
                if isinstance(target, astroid.AssignName)
            )
            and isinstance(node.value, astroid.Const)
            and node.value.value is True
        )

    def is_abstract_model(self, node):
        """
        Return True if astroid node has a Meta class with abstract = True.
        """
        # look for "class Meta"
        for element in node.body:
            if isinstance(element, astroid.ClassDef) and element.name == 'Meta':
                # look for "abstract = True"
                for inner_element in element.body:
                    if self._is_abstract_and_set_to_true(inner_element):
                        return True
        return False
