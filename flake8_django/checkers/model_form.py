import astroid

from .base_model_checker import BaseModelChecker
from .issue import Issue


class DJ06(Issue):
    code = 'DJ06'
    description = 'Do not use exclude with ModelForm, use fields instead'


class DJ07(Issue):
    code = 'DJ07'
    description = "Do not use __all__ with ModelForm, use fields instead"


class ModelFormChecker(BaseModelChecker):
    model_name_lookups = ['.ModelForm', 'django.forms.models.ModelForm']

    def checker_applies(self, node):
        return self.is_model(node)

    def is_string_dunder_all(self, element):
        """
        Return True if element is astroid.Const, astroid.List or astroid.Tuple  and equals "__all__"
        """
        assign_value = element.value
        if not isinstance(
            assign_value,
            (astroid.List, astroid.Tuple, astroid.Const),
        ):
            return False
        if isinstance(assign_value, (astroid.List, astroid.Tuple)):
            return any(
                iter_item.value == '__all__'
                for iter_item in assign_value.itered()
            )
        else:
            node_value = assign_value.value
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
            if not isinstance(body, astroid.ClassDef):
                continue
            for element in body.body:
                if not isinstance(element, astroid.Assign):
                    continue
                for target in element.targets:
                    if target.name == 'fields' and self.is_string_dunder_all(element):
                        issues.append(
                            DJ07(
                                lineno=node.lineno,
                                col=node.col_offset,
                            )
                        )
                    elif target.name == 'exclude':
                        issues.append(
                            DJ06(
                                lineno=node.lineno,
                                col=node.col_offset,
                            )
                        )
        return issues
