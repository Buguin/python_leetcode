# -*- coding:utf-8 -*-
# __author__ = 'Buguin'
from common11.Common import TreeNode


class Solution:
    @staticmethod
    def zigzagLevelOrder(root: TreeNode) -> [[int]]:
        if not root:
            return []
        ans = []
        root_list = [root]
        flag = True
        # ans = [root.val]
        while root_list:
            temp_ans = []
            temp_list = []
            for temp_root in root_list:
                # if temp_root is None:
                #     continue
                temp_ans.append(temp_root.val)
                if flag:
                    if temp_root.left:
                        temp_list.insert(0, temp_root.left)
                    if temp_root.right:
                        temp_list.insert(0, temp_root.right)
                else:
                    if temp_root.right:
                        temp_list.insert(0,temp_root.right)
                    if temp_root.left:
                        temp_list.insert(0,temp_root.left)
            if flag:
                flag = False
            else:
                flag = True
            ans.append(temp_ans)
            root_list = temp_list
        return ans
