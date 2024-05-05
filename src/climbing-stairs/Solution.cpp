// https://leetcode.com/problems/climbing-stairs


class Solution {
public:
    vector<int> stairs;
    int climb(int n){
        if(stairs[n] != -1){
            return stairs[n];
        }
        int s = climb(n - 1) + climb(n - 2);
        stairs[n] = s;
        return stairs[n];
    }
    int climbStairs(int n) {
        stairs.reserve(n + 1);
        stairs.push_back(0);
        stairs.push_back(1);
        stairs.push_back(2);
        for(int i = 3; i < n + 1; i++){
            stairs.push_back(-1);
        }
        return climb(n);
    }
};