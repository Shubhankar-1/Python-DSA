class Solution:
    def generate(numRows: int):
        n = 0
        m = 0
        pascal_triangle = []
        while(n <= numRows):
            pascal_triangle.append([1 if(m == 0 or m == n-1) else pascal_triangle[n-1][m-1]+pascal_triangle[n-1][m] for m in range(n)])
            n += 1
        return pascal_triangle[1:]


if __name__ == "__main__":
    s = Solution
    x = s.generate(numRows=5)
    print(x)
