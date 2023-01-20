from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Depth-first search (DFS)
def maxDepth(root: Optional[TreeNode]) -> int:
    return 0

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