# https://leetcode.com/problems/redundant-connection

class Solution:
    def findRedundantConnection(self, edges: [[int]]) -> [int]:
        sets = []
        for e in edges:
#            print(sets)
            f = t = -1
            for i,s in enumerate(sets):
                if(f == -1 and e[0] in s): 
                    f = i 
                if(t == -1 and e[1] in s): 
                    t = i 
                if((f != -1) and (t != -1)):
                    break
#            print(f,t)
            if(f == t == -1):
                sets.append(set([e[0],e[1]]))
            elif(f == -1 and t != -1):
                sets[t].add(e[0])
            elif(t == -1 and f != -1):
                sets[f].add(e[1])
            elif(t != f): 
#                print("YES")
                sets[f] = sets[f].union(sets[t])
                sets.pop(t)
            else:
                return e
