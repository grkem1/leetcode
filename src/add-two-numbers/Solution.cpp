// https://leetcode.com/problems/add-two-numbers

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode * l3 = new ListNode(0);
        ListNode * l1_it = l1;
        ListNode * l2_it = l2;
        ListNode * l3_it = l3;
        int carry = 0;
        while( l1_it->next != NULL && l2_it->next != NULL ){
            l3_it->val = l1_it->val + l2_it->val + carry;
            if(l3_it->val > 9){
                l3_it->val -= 10;
                carry = 1;
            }else{
                carry = 0;
            }
            l1_it = l1_it->next;
            l2_it = l2_it->next;
            l3_it->next = new ListNode(0);
            l3_it = l3_it->next;
        }
        l3_it->val = l1_it->val + l2_it->val + carry;
        if(l3_it->val > 9){
            l3_it->val -= 10;
            carry = 1;
        }else{
            carry = 0;
        }
        l1_it = l1_it->next;
        l2_it = l2_it->next;
        while( l1_it != NULL ){
            l3_it->next = new ListNode(0);
            l3_it = l3_it->next;
            l3_it->val = l1_it->val + carry;
            if(l3_it->val > 9){
                l3_it->val -= 10;
                carry = 1;
            }else{
                carry = 0;
            }
            l1_it = l1_it->next;
        }
        while( l2_it != NULL ){
            l3_it->next = new ListNode(0);
            l3_it = l3_it->next;
            l3_it->val = l2_it->val + carry;
            if(l3_it->val > 9){
                l3_it->val -= 10;
                carry = 1;
            }else{
                carry = 0;
            }
            l2_it = l2_it->next;
        }
        if(carry == 1){
            l3_it->next = new ListNode(1);
        }
        // l3_it = NULL;
        return l3;
    }
};