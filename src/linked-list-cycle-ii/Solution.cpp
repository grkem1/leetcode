// https://leetcode.com/problems/linked-list-cycle-ii

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
    ListNode *detectCycle(ListNode *head) {
        unordered_set<ListNode*> seen;
        ListNode *first = head;
        while(first != NULL){
            if(seen.find(first) == seen.end()){
                seen.insert(first);
            }else{
                return first;
            }
            first = first->next;
        }
        return NULL;     
    }
};