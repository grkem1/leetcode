// https://leetcode.com/problems/zigzag-conversion

class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 0 || numRows == 1){
            return s;
        }
        vector<string> mystrings(numRows);
        int remainder;
        int divisor = numRows * 2 - 2;
        for(int i = 0; i < s.size(); i++){
            remainder = i % divisor; 
            if(remainder <= divisor / 2){
                mystrings[remainder].push_back(s[i]);
            }else{
                mystrings[divisor - remainder].push_back(s[i]);
            }
        }
        for(int i = 1; i < mystrings.size();i++){
            mystrings[0] += mystrings[i];
        }
        return mystrings[0];
    }
};