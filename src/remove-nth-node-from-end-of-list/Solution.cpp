// https://leetcode.com/problems/remove-nth-node-from-end-of-list

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode * last = head;
        ListNode * nth = head;
        for(int i = 0; i < n; i++){
            last = last->next;
        }
        if(last == NULL){
            return head->next;
        }
        while(last->next != NULL){
            last = last->next;
            nth = nth->next;
        }
        nth->next = nth->next->next;
        return head;
    }
};