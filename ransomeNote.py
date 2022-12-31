import collections


class Solution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        count_ransomNote = collections.Counter(ransomNote)
        count_magazine = collections.Counter(magazine)

        print(count_ransomNote)
        print(count_magazine)

        for x in ransomNote:
            if count_ransomNote[x] > count_magazine[x]:
                return False

        return True


if __name__ == "__main__":
    s = Solution
    result = s.canConstruct(
        ransomNote="fihjjjjei", magazine="hjibagacbhadfaefdjaeaebgi")
    print(result)
