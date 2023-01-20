class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Depth-first search (DFS)
def maxDepth(root):
    if root is None:
        return 0
    print(f'Go down Current Node is {root.val} lets find = 1 + max( maxDepth({"None" if root.left is None else root.left.val }), maxDepth({"None" if root.right is None else root.right.val })))')

    left = maxDepth(root.left)
    right = maxDepth(root.right)
    new_depth = max(left, right) + 1
    print(f'Rollback Current Node is {root.val} new depth is {new_depth})))')
    return new_depth


if __name__ == '__main__':
    #         3
    #       /  \
    #      9    20
    #          /  \
    #         15   7
    root_instance = TreeNode(3)
    root_instance.left = TreeNode(9)
    root_instance.right = TreeNode(20)
    root_instance.right.right = TreeNode(7)
    root_instance.right.left = TreeNode(15)

    depth = maxDepth(root_instance)

    print(depth)
    print(root_instance)

    # pronoun = "he"
    num_doors = 1
    print(f'Shut the door{"s" if num_doors != 1 else ""}.')