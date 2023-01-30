class Solution:
    def carFleet(target: int, position: list[int], speed: list[int]) -> int:
        pair = [[x, y] for x, y in zip(position, speed)]
        n = len(position)
        stack = []

        for pos, sp in sorted(pair)[::-1]:
            time = (target - pos) / sp
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


s = Solution
print(s.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
