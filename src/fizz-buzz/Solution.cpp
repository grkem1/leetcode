// https://leetcode.com/problems/fizz-buzz

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> rv;
        for(int i = 1; i <= n; i++){
            string s;
            if(i % 3 == 0){
                s = "Fizz";
            }if(i % 5 == 0){
                s.insert(s.size(), "Buzz");
            }if(s.empty()){
                s = to_string(i);
            }
            rv.push_back(s);
        }
        return rv;
    }
};