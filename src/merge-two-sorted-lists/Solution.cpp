// https://leetcode.com/problems/merge-two-sorted-lists

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == NULL){
            return l2;
        }
        if(l2 == NULL){
            return l1;
        }
        ListNode * head = l1->val <= l2->val ? l1 : l2;
        ListNode n3(0);
        ListNode * next3 = &n3;
        ListNode * next1 = l1;
        ListNode * next2 = l2;
        while(true){
            while(next1 != NULL && next1->val <= next2->val){
                next3->next = next1;
                next3 = next1;
                next1 = next1->next;
            }
            if(next1 == NULL){
                next3->next = next2;
                return head;
            }
            while(next2 != NULL && next2->val <= next1->val){
                next3->next = next2;
                next3 = next2;
                next2 = next2->next;
            }
            if(next2 == NULL){
                next3->next = next1;
                return head;
            }
        }
        return head;
    }
};