import collections


class Solution:
    def isAnagram(s: str, t: str) -> bool:
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)

        if len(s) != len(t):
            return False
        else:
            for x in count_t:
                if count_s[x] != count_t[x]:
                    return False

        return True


if __name__ == "__main__":
    s = Solution()
    result = s.isAnagram(
        s="rat", t="car")
    print(result)
