// https://leetcode.com/problems/flood-fill

class Solution {
public:
    void fill(vector<vector<int>>& image, int sr, int sc, int newColor){
        if(sr > image.size() || sc > image[0].size()){
            return;
        }
        if(sr < 0 || sc < 0){
            return;
        }
        int oldColor = image[sr][sc];
        image[sr][sc] = newColor;
        if(sr > 0 && (image[sr-1][sc] == oldColor)){
            fill(image, sr-1, sc, newColor);
        }
        if( (sr < image.size()-1) && (image[sr+1][sc] == oldColor)){
            fill(image, sr+1, sc, newColor);
        }
        if(sc > 0 && (image[sr][sc-1] == oldColor)){
            fill(image, sr, sc-1, newColor);
        }
        if( (sc < image[0].size()-1) && (image[sr][sc+1] == oldColor)){
            fill(image, sr, sc+1, newColor);
        }
        
        return;
    }
    
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        if(image[sr][sc] == newColor){
            return image;
        }
        fill(image, sr, sc, newColor);
        return image;
    }
};