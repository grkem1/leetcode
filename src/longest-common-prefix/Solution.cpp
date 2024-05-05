// https://leetcode.com/problems/longest-common-prefix

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ret_s;
        int charCount = 0;
        char s;
        if(strs.size() == 0){
            return ret_s;
        }
        while(true){
            if((int)strs[0].size() - 1 < charCount){            
                return ret_s;
            }
            s = strs[0][charCount];
            for(int i = 1; i < strs.size(); i++){
                if((int)strs[i].size() - 1 < charCount){
                    return ret_s;
                }
                if(s != strs[i][charCount]){
                    return ret_s;
                }
            }
            charCount ++;
            ret_s.push_back(s);
        }
    }
};