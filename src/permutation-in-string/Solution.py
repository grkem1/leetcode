# https://leetcode.com/problems/permutation-in-string

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if(len(s2) < len(s1)):
#             return False
#         s1_id = dict((chr(i),0) for i in range(97,123))
#         window_id = dict((chr(i),0) for i in range(97,123))
#         for l in s1:
#             s1_id[l]+=1
#         for l in s2[:len(s1)]:
#             window_id[l]+=1
#         if(s1_id == window_id):
#             return True
#         next_compare = 0
#         for i in range(len(s1),len(s2)):
#             if(s2[i] not in s1_id):
#                 next_compare = len(s1)
#             window_id[s2[i]] += 1
#             window_id[s2[i-len(s1)]] -= 1
#             if(next_compare <= 0 and window_id == s1_id):
#                 return True
#             next_compare -= 1
#         return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_arr = [0]*26
        s2_arr = [0]*26
        for l in s1:
            s1_arr[ord(l) - ord('a')] += 1
        for i,l in enumerate(s2):
            s2_arr[ord(l) - ord('a')] += 1
            if(i >= len(s1)):
                s2_arr[ord(s2[i-len(s1)]) - ord('a')] -= 1
            if(s1_arr == s2_arr):
                return True
        return False
