// https://leetcode.com/problems/roman-to-integer

int char_to_int(char input){
    switch(input){
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default : return 0;
    }
}

// int value_number(const char first,const char second){
//     switch(true){
//         case (first == 'I' && second == 'V'): return -1;
//         case (first == 'I' && second == 'X'): return -1;
//         case (first == 'X' && second == 'L'): return -10;
//         case (first == 'X' && second == 'C'): return -10;
//         case (first == 'C' && second == 'D'): return -100;
//         case (first == 'C' && second == 'M'): return -100;
//     }
//     return char_to_int(first);
// }

int value_number(const char first, const char second){
    if( (first == 'I' && second == 'V') || (first == 'I' && second == 'X') ){
        return -1;
    }
    if( (first == 'X' && second == 'L') || (first == 'X' && second == 'C') ){
        return -10;
    }
    if( (first == 'C' && second == 'D') || (first == 'C' && second == 'M') ){
        return -100;
    }
    return char_to_int(first);
}

class Solution {
public:
    int romanToInt(string s) {
        int ret = 0;
        for(int i = 0; i < s.size() - 1; i++){
            ret += value_number(s[i], s[i+1]);
        }
        ret += char_to_int( s[s.size() - 1] );
        return ret;
    }
};