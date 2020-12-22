# -*- coding:utf-8 -*-
# __author__ = 'Buguin'


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def list_to_tree(s) -> TreeNode:
    tree_top = TreeNode(s.pop(0))
    tree_top_l = [tree_top]
    while s:
        tree_top_t = tree_top_l.pop(0)
        if s[0]:
            left_tree = TreeNode(s.pop(0))
            tree_top_t.left = left_tree
            tree_top_l.append(left_tree)
        else:
            s.pop(0)
        if len(s) == 0:continue
        if s[0]:
            right_tree = TreeNode(s.pop(0))
            tree_top_t.right = right_tree
            tree_top_l.append(right_tree)
        else:
            s.pop(0)
    return tree_top
