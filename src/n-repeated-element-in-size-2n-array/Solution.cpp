// https://leetcode.com/problems/n-repeated-element-in-size-2n-array

class Solution {
public:
    int repeatedNTimes(vector<int>& A) {
        unordered_set<int> uniques;
        for(int i = 0; i < A.size(); i++){
            if(uniques.find(A[i]) == uniques.end()){
                uniques.insert(A[i]);
            }else{
                return A[i];
            }
        }
        return NULL;
    }
};