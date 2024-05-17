# https://leetcode.com/problems/queue-reconstruction-by-height

class Solution:
    def reconstructQueue(self, people: [[int]]) -> [[int]]:
        h_max = 10**6+1
        queue = [[h_max,h_max]]*len(people)
        for h_i,k_i in sorted(people):
            index = 0 
            remaining_tall = k_i 
            while(remaining_tall > 0): 
                if(queue[index][0] >= h_i):
                    remaining_tall -= 1
                index += 1
            while(queue[index][0] < h_i):
                index += 1   #skip the shorter people
            queue[index] = [h_i,k_i]
#            print(queue)
        return queue
