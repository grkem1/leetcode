// https://leetcode.com/problems/perfect-squares

class Solution {
public:
    int leaps(int n, vector<int> &lsquares){
        if(lsquares[n] != -1){
            return lsquares[n];
        }
        int smallest = INT_MAX;
        for(int i = 1; n - pow(i,2) >= 0; i++){
            smallest = min(smallest, leaps(n - pow(i,2), lsquares));
        }
        lsquares[n] = smallest + 1;
        return lsquares[n];
    }
    int numSquares(int n) {
        if(n == 1){
            return 1;
        }
        vector<int> LSquares(n + 1, -1);
        LSquares[0] = 0;
        return leaps(n, LSquares);
    }
};