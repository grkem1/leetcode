// https://leetcode.com/problems/partition-list

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
    ListNode* partition(ListNode* head, int x) {
        if(head == NULL){
            return head;
        }
        ListNode * temp1 = new ListNode(0);
        ListNode * temp2 = new ListNode(0);
        ListNode * head1 = temp1;
        ListNode * head2 = temp2;
        int count = 0;
        while(head){
            count++;
            if(head == NULL) cout << "nll";
            if(head->val < x){
                temp1->next = head;
                temp1 = temp1->next;
            }else{
                temp2->next = head;
                temp2 = temp2->next;
            }
            head = head->next;
            // cout << head->val << " ";
        }
        cout << count;
        temp2->next = NULL; 
        temp1->next = head2->next;
        return head1->next;
    }
};