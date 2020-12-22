# -*- coding:utf-8 -*-
# __author__ = 'Buguin'
import unittest
from common11.SolutionTree import Solution
from common11.Common import list_to_tree


class MyTestCase(unittest.TestCase):

    def test_zigzagLevelOrder(self):
        """
        103. 二叉树的锯齿形层序遍历
        """
        s = [3,9,20,None,None,15,7]
        # s = [3, 9, 20, 5, None, 15, 7, 6]
        # s = [1,2,3,4,5]
        s = [1,2,3,4,None,None,5]
        s = [0,2,4,1,None,3,-1,5,1,None,6,None,8]
        top_tree = list_to_tree(s)
        ans = Solution.zigzagLevelOrder(top_tree)
        print(ans)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
