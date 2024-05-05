// https://leetcode.com/problems/string-to-integer-atoi

class Solution {
public:
    int myAtoi(string str) {
        long sum = 0;
        int negation = 0;
        char c;
        int i;
        bool neg = false;
        for(i = 0; i < str.size(); i++){
            if(str[i] == ' '){
                if(negation > 0){
                    return 0;
                }
                continue;
            }else if(str[i] == '-'){
                neg = true;
                negation++;
            }else if(str[i] == '+'){
                neg = false;
                negation++;
            }
            else if(str[i] < '0' || str[i] > '9' || negation > 1){
                return 0;
            }else{
                break;
            }
        }
        if( i == str.size() ){
            return 0;
        }
        for(; i < str.size(); i++){
            if(str[i] >= '0' && str[i] <= '9'){
                sum *= 10;
                if(neg){
                    sum -= ( (int)str[i] - (int)'0' );
                    if(sum < INT_MIN){
                        return INT_MIN;
                    }
                }else{
                    sum += ( (int)str[i] - (int)'0' );
                    if(sum > INT_MAX){
                        return INT_MAX;
                    }
                }
            }else{
                return sum;
            }
        }
        return sum;
    }
};