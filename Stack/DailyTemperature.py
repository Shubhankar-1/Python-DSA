class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        n = len(temperatures)

        for x in range(n):
            no_of_days = 1
            z = 0

            for y in range(x+1, n):
                if temperatures[y] > temperatures[x]:
                    z = temperatures[y]
                    break
                else:
                    no_of_days += 1

            if z > temperatures[x]:
                result.append(no_of_days)
            else:
                result.append(0)

        return result
