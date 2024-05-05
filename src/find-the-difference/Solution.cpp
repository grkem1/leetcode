// https://leetcode.com/problems/find-the-difference

class Solution {
public:
    char findTheDifference(string s, string t) {
        char added = 0;
        for(char& ss:s){
            added ^= ss;
        }
        for(char& tt:t){
            added ^= tt;
        }
        return added;
    }
};