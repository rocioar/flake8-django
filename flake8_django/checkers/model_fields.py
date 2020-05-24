from .checker import Checker
from .issue import Issue


NOT_NULL_TRUE_FIELDS = [
    'CharField', 'TextField', 'SlugField',
    'EmailField', 'UUIDField', 'ImageField',
    'FileField', 'FilePathField', 'URLField'
]


class DJ01(Issue):
    code = 'DJ01'
    description = 'Avoid using null=True on string-based fields such as CharField and TextField'


class ModelFieldChecker(Checker):

    def run(self, node):
        call_name = self.get_call_name(node)
        if call_name not in NOT_NULL_TRUE_FIELDS:
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
        return issues
