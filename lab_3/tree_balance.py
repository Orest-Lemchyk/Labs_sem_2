class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def check_balanced(root):
    ''''''
    balanced, _ = is_tree_balanced(root)
    return balanced

def is_tree_balanced(root):
    '''Перевірка, чи бінарне дерево є збалансованим деревом'''

    if root is None:
        return(True, 0)

    left_check, left_h = is_tree_balanced(root.left) if root.left else (True, 0)
    right_check, right_h = is_tree_balanced(root.right) if root.right else (True, 0)
    root_h = max(left_h, right_h) + 1

    if not left_check or not right_check:
        return (False, 0)

    if abs(left_h - right_h) > 1:
        return (False, 0)

    return(True, root_h)

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)

balanced_root = BinaryTree(1)
balanced_root.left = BinaryTree(2)
balanced_root.right = BinaryTree(3)
balanced_root.left.left = BinaryTree(4)
balanced_root.left.right = BinaryTree(5)
balanced_root.right.left = BinaryTree(6)
balanced_root.right.right = BinaryTree(7)

unbalanced_root = BinaryTree(1)
unbalanced_root.left = BinaryTree(2)
unbalanced_root.left.left = BinaryTree(3)
unbalanced_root.left.left.left = BinaryTree(4)


print("Balanced:",check_balanced(root))
print("Balanced:", check_balanced(balanced_root))
print("Unbalanced:", check_balanced(unbalanced_root))
