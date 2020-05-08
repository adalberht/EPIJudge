from collections import namedtuple
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalanceStatusWithHeight = namedtuple(
        'BalanceStatusWithHeight',
        ('is_balanced', 'height')
    )

    def check_balanced(node):
        if not node: return BalanceStatusWithHeight(True, -1)
        left_subtree = check_balanced(node.left)
        if not left_subtree.is_balanced:
            return left_subtree
        
        right_subtree = check_balanced(node.right)
        if not right_subtree.is_balanced:
            return right_subtree

        is_balanced = abs(left_subtree.height - right_subtree.height) <= 1
        height = max(left_subtree.height, right_subtree.height) + 1
        return BalanceStatusWithHeight(
            is_balanced=is_balanced,
            height=height
        )

    return check_balanced(tree).is_balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
