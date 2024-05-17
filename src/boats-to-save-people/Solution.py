# https://leetcode.com/problems/boats-to-save-people

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        total = 0
        i,j = 0,len(people)-1
        boat = 0
        while(i < j):
            if(people[j] + people[i] <= limit):
                boat = people[j] + people[i]
                j-=1
                i+=1
            else:
                boat = people[j]
                j-=1
            total += 1
        total += (i == j)
        return total