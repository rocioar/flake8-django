import ast

from .base_model_checker import BaseModelChecker
from .issue import Issue


class DJ06(Issue):
    code = 'DJ06'
    description = 'Do not use exclude with ModelForm, use fields instead'


class DJ07(Issue):
    code = 'DJ07'
    description = "Do not use __all__ with ModelForm, use fields instead"


class ModelFormChecker(BaseModelChecker):
    model_name_lookup = 'ModelForm'

    def checker_applies(self, node):
        for base in node.bases:
            is_model_form = self.is_model_name_lookup(base) or self.is_models_name_lookup_attribute(base)
            if is_model_form:
                return True
        return False

    def is_string_dunder_all(self, element):
        """
        Return True if element is ast.Str or ast.Bytes and equals "__all__"
        """
        if not isinstance(element.value, (ast.Str, ast.Bytes)):
            return False

        node_value = element.value.s
        if isinstance(node_value, bytes):
            node_value = node_value.decode()
        return node_value == '__all__'

    def run(self, node):
        """
        Captures the use of exclude in ModelForm Meta
        """
        if not self.checker_applies(node):
            return

        issues = []
        for body in node.body:
            if not isinstance(body, ast.ClassDef):
                continue
            for element in body.body:
                if not isinstance(element, ast.Assign):
                    continue
                for target in element.targets:
                    if target.id == 'fields' and self.is_string_dunder_all(element):
                        issues.append(
                            DJ07(
                                lineno=node.lineno,
                                col=node.col_offset,
                            )
                        )
                    elif target.id == 'exclude':
                        issues.append(
                            DJ06(
                                lineno=node.lineno,
                                col=node.col_offset,
                            )
                        )
        return issues
