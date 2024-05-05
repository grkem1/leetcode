// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class numChar{
    public:
    int numberCount;
    char chars[4];
    numChar(int a = 0, char b = '0', char c = '0', char d = '0', char e = '0'){
        numberCount = a;
        chars[0] = b;
        chars[1] = c;
        chars[2] = d;
        chars[3] = e;
    }
};

class Solution {
public:
    
    vector<string> addLetters(vector<string> & strings, char number, unordered_map<char, numChar>& mymap ){
        vector<string> retStrings;
        // cout << number << " " << mymap[number].numberCount << endl;
        int a = mymap[number].numberCount;
        // cout << a;
        for(int i = 0; i < strings.size(); i++){
            for(int j = 0; j < a; j++ ){
                // cout << "enter";
                retStrings.push_back(strings[i] + mymap[number].chars[j]);
                
            }
        }
        return retStrings;
    }
    vector<string> letterCombinations(string digits) {
        vector<string> retStrings;
        if(digits.size() == 0){
            return retStrings;
        }else{
            retStrings.push_back("");
        }
        unordered_map<char, numChar> mymap;
        mymap.insert({{'2', numChar{3,'a','b','c'}}, {'3', numChar{3,'d','e','f'}}, {'4', numChar{3,'g','h','i'}}, {'5', numChar{3,'j','k','l'}}, {'6', numChar{3,'m','n','o'}}, {'7', numChar{4,'p','q','r','s'}}, {'8', numChar{3, 't','u','v'}}, {'9', numChar{4,'w','x','y','z'}} });
        // cout << mymap[digits[0]].numberCount;
        for(int i = 0; i < digits.size(); i++){
            retStrings = addLetters(retStrings, digits[i], mymap);
        }
        
        return retStrings;
    }
};