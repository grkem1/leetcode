// https://leetcode.com/problems/same-tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p == NULL && q == NULL){
            return true;
        }else if(p == NULL && q != NULL || p != NULL && q == NULL){
            return false;
        }
        if(p->val != q->val){
            return false;
        }
        if(isSameTree(p->left, q->left) && isSameTree(p->right, q->right)){
            return true;
        }
        return false;
    }
};