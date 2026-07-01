class Solution(object):
    def lengthLongestPath(self, input):
        stack = {0: 0}
        ans = 0

        for line in input.split('\n'):
            depth = line.count('\t')
            name = line.lstrip('\t')

            if '.' in name:
                ans = max(ans, stack[depth] + len(name))
            else:
                stack[depth + 1] = stack[depth] + len(name) + 1

        return ans