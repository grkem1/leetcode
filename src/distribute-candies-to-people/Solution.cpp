// https://leetcode.com/problems/distribute-candies-to-people

class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        vector<int> pockets(num_people, 0);
        if(num_people == 0){
            return pockets;
        }
        int base = 0;
        while(candies > num_people * (base + num_people / 2) ){
            for(int i = 0; i < num_people; i++){
                pockets[i] += (base+i+1);
                candies -= (base+i+1);
            }
            base += num_people;
        }
        for(int i = 0; (i < num_people) && (candies > 0); i++){
            // cout << candies << " " << base << " " << i;
            pockets[i] += min(candies, base+i+1);
            candies -= min(candies, base+i+1);
        }
        return pockets;
    }
};