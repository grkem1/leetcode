// https://leetcode.com/problems/count-and-say

string c_say(const string & s){
    string output;
    char c = s[0];
    int count = 1;
    for(int i = 1; i < s.size(); i++){
        if(s[i] != c){
            output.push_back((char)(count + (int)'0'));
            output.push_back(c);
            count = 1;
            c = s[i];
        }else{
            count++;
        }
    }
    output.push_back((char)(count + (int)'0'));
    output.push_back(c);
    return output;
}

class Solution {
public:
    string countAndSay(int n) {
        if(n == 1){
            return "1";
        }
        return c_say(countAndSay(n-1));
    }
};