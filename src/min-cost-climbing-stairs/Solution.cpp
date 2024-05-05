// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution {
public:
    vector<int> cumulativeCosts;
    int costOf(int a, vector<int>& cost){
        if(cumulativeCosts[a] != -1){
            return cumulativeCosts[a];
        }
        int s = min( costOf(a-1, cost), costOf(a-2, cost) ) + cost[a];
        cumulativeCosts[a] = s;
        return s;
        
    }
    int minCostClimbingStairs(vector<int>& cost) {
        if(cost.size() == 0){
            return 0;
        }else if(cost.size() == 1){
            return cost[0];
        }else if(cost.size() == 2){
            return cost[0] < cost[1] ? cost[0] : cost[1];
        }
        cumulativeCosts.reserve(cost.size());
        cumulativeCosts.push_back(cost[0]);
        cumulativeCosts.push_back(cost[1]);
        for(int i = 2; i < cost.size(); i++){
            cumulativeCosts.push_back(-1);
        }
        int one = costOf(cost.size() - 1, cost);
        int two = costOf(cost.size() - 2, cost);
        return min(one,two);
    }
};