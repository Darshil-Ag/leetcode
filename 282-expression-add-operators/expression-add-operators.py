
class Solution(object):
    def addOperators(self, num, target):
        result = []
        n = len(num)

        def dfs(index, expression, value, last):
            if index == n:
                if value == target:
                    result.append(expression)
                return

            for i in range(index, n):
                # Avoid leading zeros
                if i > index and num[index] == '0':
                    break

                curr_str = num[index:i + 1]
                curr = int(curr_str)

                # First number: no operator
                if index == 0:
                    dfs(i + 1, curr_str, curr, curr)
                else:
                    # Addition
                    dfs(i + 1, expression + '+' + curr_str,
                        value + curr, curr)

                    # Subtraction
                    dfs(i + 1, expression + '-' + curr_str,
                        value - curr, -curr)

                    # Multiplication (handle precedence)
                    dfs(i + 1, expression + '*' + curr_str,
                        value - last + last * curr,
                        last * curr)

        dfs(0, "", 0, 0)

        return result
