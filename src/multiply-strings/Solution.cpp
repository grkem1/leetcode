// https://leetcode.com/problems/multiply-strings

class Solution {
public:
    string sum(string num1, string num2){
        if(num1.size() == 0){
            return num2;
        }
        if(num2.size() == 0){
            return num1;
        }
        if(num1 == "0"){
            return num2;
        }
        if(num2 == "0"){
            return num1;
        }
        string num3;
        int carry = 0;
        int res;
        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());
        while(num1.size() < num2.size()){
            num1.push_back('0');
        }
        while(num2.size() < num1.size()){
            num2.push_back('0');
        }
        for(int i = 0; i < num1.size(); i++){
            res = num1[i] - '0' + num2[i] - '0' + carry;
            carry = res/10;
            res = res%10;
            num3.push_back(char(res + '0'));
        }
        if(carry != 0){
            num3.push_back(char(carry + '0') );
        }
        reverse(num3.begin(), num3.end());
        return num3;
    }
    
    string multiply_singleDigit(string num, char num_single){
        string result;
        if(num_single == '0'){
            result.push_back('0');
            return result;
        }
        int res;
        int carry = 0;
        reverse(num.begin(), num.end());
        for(int i = 0; i < num.size(); i++){
            res = (num_single - '0') * (num[i] - '0') + carry;
            carry = res / 10;
            res = res % 10;
            result.push_back( char(res + '0') );
        }
        if(carry != 0){
            result.push_back( char(carry + '0') );
        }
        reverse(result.begin(), result.end());
        return result;
    }
    
    string multiply(string num1, string num2) {
        if(num1.size() == 0){
            return num2;
        }
        if(num2.size() == 0){
            return num1;
        }
        vector<string> addends;
        string result;
        // reverse(num1.begin(), num1.end());
        // reverse(num2.begin(), num2.end());
        string temp;
        string & multiplicand = num1.size() > num2.size() ? num1 : num2;
        string & multiplier = num1.size() > num2.size() ? num2 : num1;
        for(int i = multiplier.size() - 1; i >= 0; i--){
            temp = multiply_singleDigit( multiplicand , multiplier[i] );
            for(int j = multiplier.size() - 1; j > i; j--){
                temp.push_back('0');
            }
            addends.push_back(temp);
        }
        for(int i = 0; i < addends.size(); i++){
            result = sum( result , addends[i] );
        }
        return result;
    }
};