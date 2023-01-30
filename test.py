<<<<<<< HEAD
x = y = None

y= 30

print("x", x)
print("y", y)
=======
def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    l = 0
    output = 0
    for r in range(len(s)):
        if s[r] not in seen:
            output = max(output, r-l + 1)
        else:
            if seen[s[r]] < l:
                output = max(output, r-l + 1)
            else:
                l = seen[s[r]] + 1

        seen[s[r]] = r

    return output


print(lengthOfLongestSubstring(s="pwwkew"))
>>>>>>> e46afbe (added files)
