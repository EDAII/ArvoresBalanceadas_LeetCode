class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left = max(0, left)
            right = max(0, right)

            current_sum = node.val + left + right
            self.max_sum = max(self.max_sum, current_sum)

            return node.val + max(left, right)

        dfs(root)
        return self.max_sum
