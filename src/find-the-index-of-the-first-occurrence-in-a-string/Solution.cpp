// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.size() == 0){
            return 0;
        }
        if(needle.size() > haystack.size()){
            return -1;
        }
        char c = needle[0];
        for(int i = 0; i < haystack.size() - needle.size() + 1; i++){
            if(haystack[i] == c){
                if(haystack.substr(i+1,needle.size()-1).compare(needle.substr(1,needle.size()-1)) == 0){
                    return i;
                }
            }
        }
        return -1;
    }
};