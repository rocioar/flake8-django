from .checker import Checker
from .issue import Issue


NOT_NULL_TRUE_FIELDS = [
    'CharField', 'TextField', 'SlugField',
    'EmailField', 'UUIDField', 'ImageField',
    'FileField', 'FilePathField', 'URLField'
]
NOT_BLANK_TRUE_FIELDS = ['BooleanField']
FOREIGN_KEY_FIELDS = ['ForeignKey', 'ManyToManyField']


class DJ01(Issue):
    code = 'DJ01'
    description = 'null=True not recommended to be used in {field}'


class DJ02(Issue):
    code = 'DJ02'
    description = 'blank=True not recommended to be used in {field}'


class DJ12(Issue):
    code = 'DJ12'
    description = 'related_name not set in {field}'


class ModelFieldChecker(Checker):

    def run(self, node):
        call_name = self.get_call_name(node)
        if call_name not in (NOT_NULL_TRUE_FIELDS + NOT_BLANK_TRUE_FIELDS + FOREIGN_KEY_FIELDS):
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

        if call_name in FOREIGN_KEY_FIELDS:
            related_name_found = False
            for keyword in node.keywords:
                if 'related_name' in keyword.arg:
                    related_name_found = True
            if not related_name_found:
                issues.append(
                    DJ12(
                        lineno=node.lineno,
                        col=node.col_offset,
                        parameters={'field': call_name}
                    )
                )
        return issues
