// https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        high,low = n,1
        if(isBadVersion(low)):
            return low
        while(high>low+1):
            suspect = (high+low)//2
            if(isBadVersion(suspect)):
                high = suspect
            else:
                low = suspect
        return high