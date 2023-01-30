
class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'(': ')', '[': ']', '{': '}'}

        if len(s) % 2 != 0:
            return False
        else:
            for x in s:
                if x in dict: 
                    stack.append(x)
                elif len(stack)>0 or dict[stack.pop()] != x:
                    return False 

        
        return len(stack) ==0


if __name__ == "__main__":
    s = Solution()
    result = s.isValid(s="{[]}")
    print(result)
