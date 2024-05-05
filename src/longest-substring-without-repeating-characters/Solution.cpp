// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.empty()){
            return 0;
        }
        int max = 1;
        int count = 1;
        bool crop = false;
        for(int i = 1; i < s.size(); i++){
            crop = false;
            for(int j = i - count; j < i; j++){
                if(s[i] == s[j]){
                    count = i - j;
                    crop = true;
                }
            }
            if(crop == false){
                count++;
            }
            if(count > max){
                max = count;
            }
        }
        return max;
    }
};