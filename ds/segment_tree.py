class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = None
        self.left = None
        self.right = None


def build(a, l, r, fn):
    if l > r:
        return None
    result = SegmentTreeNode(l, r)
    if l == r:
        result.value = a[l]
    else:
        m = (l + r) // 2
        result.left = build(a, l, m, fn)
        result.right = build(a, m + 1, r, fn)
        if result.left is not None and result.right is not None:
            result.value = fn(result.left.value, result.value)
        elif result.left is not None:
            result.value = result.left.value
        else:
            result.value = result.right.value
    return result


def query(tree, l, r, fn):
    if tree is None:
        return None
    if l <= tree.start and tree.end <= r:
        return tree.value
    if tree.end < l:
        return None
    if r < tree.start:
        return None
    return fn(query(tree.left, l, r, fn), query(tree.right, l, r, fn))


def update(tree, i, value, fn):
    if tree is None:
        return None
    if tree.end < i:
        return tree.value
    if i < tree.start:
        return tree.value
    if tree.start == tree.end and tree.start == i:
        tree.value = value
    else:
        a = update(tree.left, i, value, fn)
        b = update(tree.right, i, value, fn)
        tree.value = fn(a , b)
    return tree.value
