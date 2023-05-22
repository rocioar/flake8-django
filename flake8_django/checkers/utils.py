import astroid


def node_is_subclass(node, subclass_names):
    """Checks if node has parent with any class from subclass_names."""
    if not isinstance(node, (astroid.ClassDef, astroid.Instance)):
        return False

    if node.bases == astroid.Uninferable:
        return False  # pragma: no cover
    for base_cls in node.bases:
        try:
            for inf in base_cls.inferred():
                if inf.qname() in subclass_names:
                    return True
                if inf != node and node_is_subclass(inf, subclass_names):
                    return True
        except astroid.InferenceError:  # pragma: no cover
            continue

    return False
