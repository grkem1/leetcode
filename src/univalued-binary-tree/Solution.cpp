// https://leetcode.com/problems/univalued-binary-tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

bool traceUni(TreeNode * node, int value){
    if(node == NULL){
        return true;
    }
    if(node->val != value){
        return false;
    }
    return ( traceUni(node->left, value) && traceUni(node->right,value) );
}

class Solution {
public:
    bool isUnivalTree(TreeNode* root) {
        int value = root->val;
        return ( traceUni(root->left, value) && traceUni(root->right,value) );
    }
};