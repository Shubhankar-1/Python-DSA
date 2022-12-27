class Solution:
    def searchMatrix(matrix: list[list[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for x in range(n):
            if target <= matrix[x][m-1]:
                if target in matrix[x]:
                    return True
        return False


if __name__ == "__main__":
    s = Solution
    result = s.searchMatrix(
        matrix=[[1], [3]], target=1)
    print(result)
