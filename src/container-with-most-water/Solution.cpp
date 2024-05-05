// https://leetcode.com/problems/container-with-most-water

class Solution {
public:
    int maxArea(vector<int>& height) {
        vector<int>& a = height;
        if(height.size() < 2){
            return 0;
        }
        int ii, jj, i, j;
        i = ii = 0;
        j = jj = height.size() - 1;
        int area = (j - i) * min(a[j], a[i]);
        while(j > i){
            if(a[i] > a[j]){
                --j;
                if( min(a[j], a[i]) * (j - i) > area ){
                    area = min(a[j], a[i]) * (j - i);
                }
            }else{
                ++i;
                if( min(a[j], a[i]) * (j - i) > area ){
                    area = min(a[j], a[i]) * (j - i);
                }
            }
        }
        return area;
    }
};