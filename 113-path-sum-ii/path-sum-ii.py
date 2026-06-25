class Solution(object):
    def pathSum(self, root, targetSum):
        ans = []

        def dfs(node, target, path):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right and target == node.val:
                ans.append(path[:])
            else:
                dfs(node.left, target - node.val, path)
                dfs(node.right, target - node.val, path)

            path.pop()

        dfs(root, targetSum, [])
        return ans