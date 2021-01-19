from .checker import Checker
from .issue import Issue


NOT_NULL_TRUE_FIELDS = [
    'CharField', 'TextField', 'SlugField',
    'EmailField', 'FilePathField', 'URLField'
]


class DJ01(Issue):
    code = 'DJ01'
    description = 'Avoid using null=True on string-based fields such {field}.'


class ModelFieldChecker(Checker):

    def run(self, node):
        call_name = self.get_call_name(node)
        if call_name not in NOT_NULL_TRUE_FIELDS:
            return

        found_null_true = False
        found_unique_true = False
        found_blank_true = False
        issues = []
        for keyword in node.keywords:
            if keyword.arg == 'null' and getattr(keyword.value, 'value', False) is True:
                found_null_true = True

            if keyword.arg == 'unique' and getattr(keyword.value, 'value', False) is True:
                found_unique_true = True

            if keyword.arg == 'blank' and getattr(keyword.value, 'value', False) is True:
                found_blank_true = True

            # consider exception for the rule when unique=True and blank=True
            if found_blank_true and found_unique_true:
                return

        if found_null_true:
            issues.append(
                DJ01(
                    lineno=node.lineno,
                    col=node.col_offset,
                    parameters={'field': call_name}
                )
            )
        return issues
