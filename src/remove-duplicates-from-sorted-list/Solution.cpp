// https://leetcode.com/problems/remove-duplicates-from-sorted-list

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* index = head;
        if(index == NULL){
            return index;
        }
        while(true){
            if(index->next == NULL){
                break;
            }
            else if(index->next->val == index->val){
                index->next = index->next->next;
            }
            else{
                index = index->next;
            }
        }
        return head;
    }
};