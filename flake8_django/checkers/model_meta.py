import astroid

from flake8_django.checkers.base_model_checker import BaseModelChecker
from flake8_django.checkers.issue import Issue


class DJ10(Issue):
    code = 'DJ10'
    description = 'Model should define verbose_name in its Meta inner class'


class DJ11(Issue):
    code = 'DJ11'
    description = 'Model should define verbose_name_plural in its Meta inner class'


class ModelMetaChecker(BaseModelChecker):
    model_name_lookups = ['.Model', 'django.db.models.base.Model']

    def checker_applies(self, node):
        return self.is_model(node) and not self.is_abstract_model(node)

    def get_meta_class(self, node):
        for child_node in node.body:
            if isinstance(child_node, astroid.ClassDef):
                if child_node.name == 'Meta':
                    return child_node
        return

    def _has_element(self, node, target_name: str):
        for child_node in node.body:
            if not isinstance(child_node, astroid.Assign):
                continue
            attr = child_node.targets[0].name
            if attr == target_name:
                return True
        return False

    def has_verbose_name(self, meta_class_node):
        return self._has_element(meta_class_node, 'verbose_name')

    def has_verbose_name_plural(self, meta_class_node):
        return self._has_element(meta_class_node, 'verbose_name_plural')

    def run(self, node):
        if not self.checker_applies(node):
            return

        meta_class_node = self.get_meta_class(node)
        issues = []
        if not meta_class_node or not self.has_verbose_name(meta_class_node):
            issues.append(
                DJ10(
                    lineno=node.lineno,
                    col=node.col_offset,
                )
            )

        if not meta_class_node or not self.has_verbose_name_plural(meta_class_node):
            issues.append(
                DJ11(
                    lineno=node.lineno,
                    col=node.col_offset,
                )
            )

        return issues
