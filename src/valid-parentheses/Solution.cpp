// https://leetcode.com/problems/valid-parentheses


bool doesMatch(char i1, char i2){
    if( (i1 == '[' && i2 == ']') || (i1 == ']' && i2 == '[') ){
        return true;
    }
    if( (i1 == '(' && i2 == ')') || (i1 == ')' && i2 == '(') ){
        return true;
    }
    if( (i1 == '{' && i2 == '}') || (i1 == '}' && i2 == '{') ){
        return true;
    }
    return false;
}

bool isClosing(char input){
    if( (input == '}') || (input == ')') || (input == ']') ){
        return true;
    }else{
        return false;
    }
}

class Solution {
public:
    bool isValid(string s) {
        char c;
        stack<char> symbols;
        while(!s.empty()){
            c = s.back();
            s.pop_back();
            if(isClosing(c)){
                symbols.push(c);
            }else{
                if(symbols.empty()){
                    return false;
                }else{
                    if(doesMatch(c, symbols.top())){
                        symbols.pop();
                    }else{
                        return false;
                    }
                }
            }
        }
        if(symbols.empty()){
            return true;
        }else{
            return false;
        }
    }
};