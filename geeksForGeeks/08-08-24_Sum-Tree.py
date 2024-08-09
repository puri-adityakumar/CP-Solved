
# https://www.geeksforgeeks.org/problems/sum-tree/1
class Solution:

    def solve(self,root):

        if not root: return [True,0]

        if not root.left and not root.right: return [True,root.data]

        lt = self.solve(root.left)
        rt = self.solve(root.right)

        if lt[0] and rt[0] and root.data == (lt[1]+rt[1]):
            return [True,root.data * 2]

        return [False,lt[1] + rt[1]]


    def is_sum_tree(self, node): return self.solve(node)[0]
