import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        removed_items = {}
        for x in range(len(s)):
            if (s[x] not in dict) and (s[x] not in removed_items):
                dict[s[x]] = x
            elif s[x] not in removed_items:
                removed_items[s[x]] = x
                dict.pop(s[x])

        if len(dict) == 0:
            return -1
        else:
            return next(iter(dict.values()))


if __name__ == "__main__":
    s = Solution()
    result = s.firstUniqChar(s="aadadaud")
    print(result)
    
