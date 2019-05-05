from ast import Assign, Call, ClassDef, FunctionDef

from .base_model_checker import BaseModelChecker
from .issue import Issue


class DJ09(Issue):
    code = 'DJ09'
    description = 'Order of model inner classes and standard methods does not follow Django style guide: {elem_type} should come before {before}'

    def __init__(self, elem, elem_type, before):
        super().__init__(elem.lineno, elem.col_offset, None)
        self.description = self.description.format(
            elem_type=elem_type,
            before=before,
        )


def is_assignment_call(node):
    return isinstance(node, Assign) and isinstance(node.value, Call)


def is_manager_declaration(node):
    return isinstance(node, Assign) and node.targets[0].id == 'objects'


def is_meta_declaration(node):
    return isinstance(node, ClassDef) and node.name == 'Meta'


def is_save_declaration(node):
    return isinstance(node, FunctionDef) and node.name == 'save'


def is_str_declaration(node):
    return isinstance(node, FunctionDef) and node.name == '__str__'


def is_url_declaration(node):
    return isinstance(node, FunctionDef) and node.name == 'get_absolute_url'


class ModelContentOrderChecker(BaseModelChecker):
    model_name_lookup = 'Model'

    def checker_applies(self, node):
        for base in node.bases:
            if self.is_model_name_lookup(base) or self.is_models_name_lookup_attribute(base):
                return True
        return False

    def get_elem_linenos(self, node):
        # expected order of each element type
        order = [
            'field declaration',
            'manager declaration',
            'Meta class',
            '__str__ method',
            'save method',
            'get_absolute_url method',
            'custom method',
        ]

        found_idx = []
        for elem in node.body:
            # determine each element type
            if is_manager_declaration(elem):
                elem_type = 'manager declaration'
            elif is_meta_declaration(elem):
                elem_type = 'Meta class'
            elif is_str_declaration(elem):
                elem_type = '__str__ method'
            elif is_save_declaration(elem):
                elem_type = 'save method'
            elif is_url_declaration(elem):
                elem_type = 'get_absolute_url method'
            elif isinstance(elem, FunctionDef):
                elem_type = 'custom method'
            elif is_assignment_call(elem):
                # assignment to the return value of a function call is presumed to be a field
                elem_type = 'field declaration'
            else:
                # skip unknowns
                continue  # pragma: no cover

            # get the expected order of elem_type. find the first index which is greater than elem_idx. if any such
            # index was found, the element type corresponding to that index should have come before ``elem``.
            # otherwise, add the index of elem_type to the list of found indices.
            elem_idx = order.index(elem_type)
            greater_idx = next((i for i in found_idx if i > elem_idx), -1)
            if greater_idx > -1:
                before = order[greater_idx]
                yield DJ09(
                    elem,
                    elem_type,
                    before,
                )
            else:
                found_idx.append(elem_idx)

    def run(self, node):
        if not self.checker_applies(node):
            return

        return list(self.get_elem_linenos(node))
