// https://leetcode.com/problems/linked-list-cycle

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
    bool hasCycle(ListNode *head) {
        if(head == NULL){
            return false;
        }
        unordered_set<ListNode* > pointers;
        pointers.insert(head);
        ListNode *index = head;
        while(index->next != NULL){
            index = index->next;
            if(pointers.find(index) == pointers.end()){
                pointers.insert(index);            
            }else{
                return true;
            }    
        }
        return false;
    }
};