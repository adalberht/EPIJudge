from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def traverse(node, result):
    if node:
        traverse(node.left, result)
        result.append(node.data)
        traverse(node.right, result)
        return result
    return result

def find_min(node):
    return min(traverse(node, []))


def find_max(node):
    return max(traverse(node, []))

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # traversal = traverse(tree, [])
    # for i in range(1, len(traversal)):
    #     if traversal[i] < traversal[i-1]: return False
    # return True
    if not tree: return True

    if tree.left and (tree.data < find_max(tree.left) or not is_binary_tree_bst(tree.left)):
        return False
    
    if tree.right and (tree.data > find_min(tree.right) or not is_binary_tree_bst(tree.right)):
        return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
