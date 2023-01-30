class Solution:
    def generateParenthesis(self, n=3) :
        stack = []
        result = []
        def backtracking(open, close):
            # 1. IF OPEN AND CLOSE PARENTHESES EQUALS TO n APPEND IT TO STACK
            if open == close == n:
                result.append("".join(stack))
                return
            # 2. IF OPEN PARENTHESES < n ADD OPEN PARENTHESES TO STACK
            if open < n:
                stack.append('(')
                backtracking(open+1, close)
                stack.pop()
            # 3. IF CLOSE PARENTHESES < OPEN PARENTHESES ADD CLOSING PARENTHESES TO STACK
            if close < open:
                stack.append(')')
                backtracking(open, close+1)
                stack.pop()
        backtracking(0, 0)
        return (result)
s = Solution()
print(s.generateParenthesis(3))
