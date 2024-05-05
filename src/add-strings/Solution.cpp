// https://leetcode.com/problems/add-strings

class Solution {
public:
    string addStrings(string num1, string num2) {
        if(num1.size() == 0){
            return num2;
        }
        if(num2.size() == 0){
            return num1;
        }
        int carry = 0;
        int res = 0;
        bool add_num1 = false;
        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());
        string num3;
        if(num1.size() > num2.size()){
            num3 = num1;
            add_num1 = false;
        }else{
            num3 = num2;
            add_num1 = true;
        }
        string & addend = add_num1 ? num1 : num2;
        int i;
        for(i = 0; i < addend.size(); i++){
            res = num3[i] - '0' + addend[i] - '0' + carry;
            carry = res / 10;
            num3[i] = (res % 10 + '0');
        }
        while(carry > 0 && i < num3.size()){
            res = num3[i] - '0' + carry;
            carry = res / 10;
            num3[i] = ( res % 10 + '0') ;
            i++;
        }
        if(carry > 0){
            num3.push_back( (carry + '0') );
        }
        reverse(num3.begin(), num3.end());
        return num3;
    }
};