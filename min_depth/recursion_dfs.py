import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Depth-first search (DFS)
def minDepth(root):
    if not root:
        return 0

    children = [root.left, root.right]
    # if we're at leaf node
    if not any(children):
        print(f'No child for node = {root.val}')
        return 1

    #         3
    #       /  \
    #      9    20
    #          /  \
    #         15   7

    min_depth = sys.maxsize
    for c in children:
        if c:
            new_min_depth = minDepth(c)
            print(f'Compare {new_min_depth} and {min_depth} for value = {root.val}')
            min_depth = min(new_min_depth, min_depth)
            print(f'New min value {new_min_depth} for value = {root.val}')
    return min_depth + 1


if __name__ == '__main__':
    root_instance = TreeNode(3)
    root_instance.left = TreeNode(9)
    root_instance.right = TreeNode(20)
    root_instance.right.right = TreeNode(7)
    root_instance.right.left = TreeNode(15)

    depth = minDepth(root_instance)

    print(depth)
    print(root_instance)
