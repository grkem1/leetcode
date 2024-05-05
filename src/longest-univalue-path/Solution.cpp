// https://leetcode.com/problems/longest-univalue-path

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
    int max = 0;
    int longestUnivaluePath(TreeNode* root){
        if(root == NULL){
            return 0;
        }
        longestUnivaluePath0(root);
        return max;
    }
    int longestUnivaluePath0(TreeNode* root) {
        int right = 0;
        int left = 0;
        bool isFound = false;
        if(root->right != NULL){
            right = longestUnivaluePath0(root->right) + 1;
            if(root->right->val == root->val){
                isFound = true;
            }else{
                right = 0;
            }
        }    
        if(root->left != NULL){
            left = longestUnivaluePath0(root->left) + 1;
            if(root->left->val == root->val){
                isFound = true;
            }else{
                left = 0;
            }
        }
        if(!isFound){
            return 0;
        }else{
            if(left + right > max){
                max = left + right;
            }
            if(left > right){
                return left;
            }else{
                return right;
            }
        }
    }
};