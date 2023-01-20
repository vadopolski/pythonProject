import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def minDepth(root):
    if not root:
        print(f'No child for node = {root.val}')
        return 0
    else:
        stack = [(1, root)]
        min_depth = sys.maxsize

    #         3
    #       /  \
    #      9    20
    #          /  \
    #         15   7

    while stack:
        depth, root = stack.pop()
        children = [root.left, root.right]
        if not any(children):
            print(f'Compare {min_depth} and {depth} for value = {root.val}')
            min_depth = min(depth, min_depth)
            print(f'New min value {min_depth} for value = {root.val}')
        for c in children:
            if c:
                stack.append((depth + 1, c))

    return min_depth

if __name__ == '__main__':
    root_instance = TreeNode(3)
    root_instance.left = TreeNode(9)
    root_instance.right = TreeNode(20)
    root_instance.right.right = TreeNode(7)
    root_instance.right.left = TreeNode(15)

    depth = minDepth(root_instance)

    print(depth)
    print(root_instance)
