class Solution(object):
    def restoreIpAddresses(self, s):
        ans = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    ans.append(".".join(path))
                return

            for i in xrange(1, 4):
                if start + i > len(s):
                    break

                part = s[start:start + i]

                if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                    continue

                path.append(part)
                backtrack(start + i, path)
                path.pop()

        backtrack(0, [])
        return ans