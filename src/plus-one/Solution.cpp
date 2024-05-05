// https://leetcode.com/problems/plus-one

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> rv;
        bool allNine = true;
        int countNines = 0;
        int carry = 0;
        if(digits.size() == 0){
            return rv;
        }
        for(int i = 0; i < digits.size(); i++){
            if(digits[i] != 9){
                allNine = false;
                break;
            }
        }
        if(allNine){
            rv.push_back(1);
            for(int i = 0; i < digits.size();i++){
                rv.push_back(0);
            }
            return rv;
        }
        for(int i = digits.size() - 1; i >= 0; i--){
            if(digits[i] == 9){
                countNines++;
            }else{
                break;
            }
        }
        if(countNines == 0){
            rv = digits;
            rv[rv.size()-1]++;
            return rv;
        }
        int index = 0;
        for(; index < digits.size() - countNines - 1; index++){
            rv.push_back(digits[index]);
        }
        rv.push_back(++digits[index++]);
        for(; index < digits.size(); index++){
            rv.push_back(0);
        }
        return rv;
    }
};