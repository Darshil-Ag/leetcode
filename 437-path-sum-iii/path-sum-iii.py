from collections import defaultdict

class Solution(object):
    def pathSum(self, root, targetSum):
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node, curr):
            if not node:
                return 0

            curr += node.val
            ans = prefix[curr - targetSum]

            prefix[curr] += 1
            ans += dfs(node.left, curr)
            ans += dfs(node.right, curr)
            prefix[curr] -= 1

            return ans

        return dfs(root, 0)