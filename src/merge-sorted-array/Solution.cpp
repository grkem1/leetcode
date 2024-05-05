// https://leetcode.com/problems/merge-sorted-array

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int index_1 = 0;
        int index_2 = 0;
        vector<int> nums3;
        int A, B;
        for(int i=0; i < n + m; i++){
            A = index_1 < m ? nums1[index_1] : INT_MAX;
            B = index_2 < n ? nums2[index_2] : INT_MAX;
            if(A < B){
                nums3.push_back(A);
                index_1++;
            }else{
                nums3.push_back(B);
                index_2++;
            }
        }
        nums1 = nums3;
    }
};