class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs_recursive(root):
    if root is None:
        return []
    left = dfs_recursive(root.left)
    right = dfs_recursive(root.right)
    return [root.val, *left, *right]

def dfs_iterative(root):
    if root is None:
        return []
    values = [root]
    res = []
    while values:
        curr = values.pop()
        res.append(curr.val)
        if curr.right:
            values.append(curr.right)
        if curr.left:
            values.append(curr.left)
    return res

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(dfs_recursive(a))
print(dfs_iterative(a))
