// https://leetcode.com/problems/island-perimeter

class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int perimeter = 0;
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[i].size(); j++){
                if(grid[i][j] == 0){
                    continue;
                }
                int contribution = 4;
                if(i > 0){
                    if(grid[i-1][j] == 1){
                        contribution--;
                    }
                }
                if(i < grid.size() - 1){
                    if(grid[i+1][j] == 1){
                        contribution--;
                    }
                }
                if(j < grid[i].size() - 1){
                    if(grid[i][j+1] == 1){
                        contribution--;
                    }
                }
                if(j > 0){
                    if(grid[i][j-1] == 1){
                        contribution--;
                    }
                }
                perimeter+= contribution;
            }
        }
        return perimeter;
    }
};