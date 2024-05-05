// https://leetcode.com/problems/longest-palindromic-substring

class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size() == 1){
            return s;
        }
        int max = 0;
        string rv;
        int i_r;
        for(int i_l=0; i_l < s.size(); i_l++){
            for(i_r=i_l + 1; i_r < s.size() && s[i_r] == s[i_l]; i_r++);
            if(i_r >= s.size() || s[i_r] != s[i_l]){
                i_r --;
            }
            if( (i_r - i_l + 1) > max ){
                max = i_r - i_l + 1;
                rv = s.substr(i_l, max);
            }
            for(int j = 1; (i_r + j < s.size() ) && ( i_l - j >= 0 ); j++ ){
                if(s[i_r+j] == s[i_l-j]){
                    if(i_r - i_l + 2*j + 1 > max){
                        max = i_r - i_l + 2*j + 1;
                        rv = s.substr(i_l-j,max);
                        // cout << i_l << " " << i_r;
                    }
                }else{
                    break;
                }
            }
        }
        return rv;
    }
};