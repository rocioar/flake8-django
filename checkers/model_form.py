import ast

from .checker import Checker
from .issue import Issue


class DJ06(Issue):
    code = 'DJ06'
    description = 'ModelForm.Meta should not set exclude, set fields instead'


class DJ07(Issue):
    code = 'DJ07'
    description = "ModelForm.Meta should not set fields to '__all__'"


class ModelFormChecker(Checker):

    def checker_applies(self, node):
        for base in node.bases:
            if self.is_model_form_attribute(base) or self.is_model_form_name(base):
                return True
        return False

    def is_model_form_name(self, base):
        return (
            isinstance(base, ast.Name) and
            base.id == 'ModelForm'
        )

    def is_model_form_attribute(self, base):
        return (
            isinstance(base, ast.Attribute) and
            isinstance(base.value, ast.Name) and
            base.value.id == 'models' and base.attr == 'ModelForm'
        )

    def is_fields_string(self, element):
        return (
            isinstance(element, ast.Expr) and
            isinstance(element.value, ast.Compare) and
            isinstance(element.value.left, ast.Name) and
            isinstance(element.value.comparators[0], ast.Str) and
            element.value.left.id == 'fields' and element.value.comparators[0].s == '__all__'
        )

    def run(self, node):
        """
        Captures the use of exclude in ModelForm Meta
        """
        if not(self.checker_applies(node)):
            return

        issues = []
        for body in node.body:
            if not isinstance(body, ast.ClassDef):
                continue
            for element in body.body:
                if self.is_fields_string(element):
                    issues.append(
                        DJ07(
                            lineno=node.lineno,
                            col=node.col_offset,
                        )
                    )
                    continue
                if not isinstance(element, ast.Assign):
                    continue
                for target in element.targets:
                    if target.id == 'exclude':
                        issues.append(
                            DJ06(
                                lineno=node.lineno,
                                col=node.col_offset,
                            )
                        )
        return issues
