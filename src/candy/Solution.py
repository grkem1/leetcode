// https://leetcode.com/problems/candy

class Solution:
    def candy(self, ratings: [int]) -> int:
        c=[1]*len(ratings)
        s=0 
        for i in range(1,len(ratings)):
            if(ratings[i]>ratings[i-1]):
                c[i]=c[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if(ratings[i+1]<ratings[i]):
                c[i]=max(c[i],c[i+1]+1)
            s+=c[i]
        return s+c[-1]
