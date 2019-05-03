import django
from .checker import Checker
from .issue import Issue


ALLOW_NULL_BOOLEAN = django.VERSION >= (2, 1)

NOT_NULL_TRUE_FIELDS = [
    'CharField', 'TextField', 'SlugField', 'EmailField', 'Field',
    'UUIDField', 'ImageField', 'FileField'
]
NOT_BLANK_TRUE_FIELDS = []

if not ALLOW_NULL_BOOLEAN:
    NOT_NULL_TRUE_FIELDS.append('BooleanField')
    NOT_BLANK_TRUE_FIELDS.append('BooleanField')


class DJ01(Issue):
    code = 'DJ01'
    description = 'null=True not recommended to be used in {field}'


class DJ02(Issue):
    code = 'DJ02'
    description = 'blank=True not recommended to be used in {field}'


class ModelFieldChecker(Checker):

    def run(self, node):
        call_name = self.get_call_name(node)
        if not(call_name in NOT_NULL_TRUE_FIELDS or call_name in NOT_BLANK_TRUE_FIELDS):
            return

        issues = []
        for keyword in node.keywords:
            if call_name in NOT_NULL_TRUE_FIELDS and keyword.arg == 'null' and keyword.value.value is True:
                issues.append(
                    DJ01(
                        lineno=node.lineno,
                        col=node.col_offset,
                        parameters={'field': call_name}
                    )
                )
            if call_name in NOT_BLANK_TRUE_FIELDS and keyword.arg == 'blank' and keyword.value.value is True:
                issues.append(
                    DJ02(
                        lineno=node.lineno,
                        col=node.col_offset,
                        parameters={'field': call_name}
                    )
                )
        return issues
