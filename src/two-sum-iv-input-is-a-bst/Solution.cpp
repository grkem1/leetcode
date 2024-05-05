// https://leetcode.com/problems/two-sum-iv-input-is-a-bst

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
    unordered_map<int,bool> numbers;
    bool findTarget(TreeNode* root, int k) {
        if(root == NULL){
            return false;
        }
        if( numbers.find(k - root->val) != numbers.end() ){
            return true;
        }
        numbers[root->val] = true;
        return( findTarget( root->right, k ) || findTarget( root->left, k ) );
    }
};