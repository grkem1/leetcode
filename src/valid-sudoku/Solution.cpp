// https://leetcode.com/problems/valid-sudoku

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Check 3x3 squares
        vector<bool> seen(9,false);
        for(int row_start = 0; row_start < 9; row_start += 3){
            for(int column_start = 0; column_start < 9; column_start += 3){
                fill(seen.begin(), seen.end(), false); // reset seen
                for(int row = row_start; row < row_start + 3; row++){
                    for(int column = column_start; column < column_start + 3; column++){
                        if(board[row][column] != '.'){
                            if(seen[ board[row][column] - '1' ] == true ){
                                // cout << row << " " << column;
                                return false;
                            }else{
                                seen[ board[row][column] - '1' ] = true;
                            }
                        }
                    }
                }
            }
        }
        // Check Rows
        for(int row = 0; row < 9; row++){
            fill(seen.begin(), seen.end(), false);
            for(int column = 0; column < 9; column++){
                if(board[row][column] != '.'){
                    if(seen[ board[row][column] - '1' ] == true ){
                        return false;
                    }else{
                        seen[ board[row][column] - '1' ] = true;
                    }
                }
            }
        }
        // Check Columns
        for(int column = 0; column < 9; column++){
            fill(seen.begin(), seen.end(), false);
            for(int row = 0; row < 9; row++){
                if(board[row][column] != '.'){
                    if(seen[ board[row][column] - '1' ] == true ){
                        return false;
                    }else{
                        seen[ board[row][column] - '1' ] = true;
                    }
                }
            }
        }
        return true;
    }
};