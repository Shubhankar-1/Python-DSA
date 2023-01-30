class Solution:
    def isValidSudoku(board):

        n = len(board)
        for x in range(n):
            row = {}
            column = {}
            cube = {}
            for y in range(n):

                # check for rows
                if board[x][y] != '.':
                    if board[x][y] not in row:
                        row[board[x][y]] = y
                    else:
                        return False

                # check for columns
                if board[y][x] != '.':
                    if board[y][x] not in column:
                        column[board[y][x]] = y
                    else:
                        return False

                # check for 3x3 cube
                cubeRow = 3*int(x/3) + int(y/3)
                cubeCol = 3*int(x % 3) + int(y % 3)
                if board[cubeRow][cubeCol] != '.':
                    if board[cubeRow][cubeCol] not in cube:
                        cube[board[cubeRow][cubeCol]] = y
                    else:
                        return False

        return True


if __name__ == "__main__":
    s = Solution
    result = s.isValidSudoku(board=[["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
                             "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
    print(result)
