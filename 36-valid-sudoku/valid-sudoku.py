
class Solution:
    def isValidSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                num = board[i][j]

                # Empty cell ko skip karo
                if num == ".":
                    continue

                # Find which 3x3 box
                boxIndex = (i // 3) * 3 + (j // 3)

                # Check duplicate
                if (num in rows[i] or
                    num in cols[j] or
                    num in boxes[boxIndex]):

                    return False

                # Store number
                rows[i].add(num)
                cols[j].add(num)
                boxes[boxIndex].add(num)

        return True
