
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        unordered_set<char> rows[9];
        unordered_set<char> cols[9];
        unordered_set<char> boxes[9];

        for(int i = 0; i < 9; i++) {

            for(int j = 0; j < 9; j++) {

                char num = board[i][j];

                // Empty cell: skip
                if(num == '.') {
                    continue;
                }

                // Find 3x3 box
                int boxIndex = (i / 3) * 3 + (j / 3);

                // Check duplicates
                if(rows[i].count(num) ||
                   cols[j].count(num) ||
                   boxes[boxIndex].count(num)) {

                    return false;
                }

                // Store the number
                rows[i].insert(num);
                cols[j].insert(num);
                boxes[boxIndex].insert(num);
            }
        }

        return true;
    }
};
