// https://leetcode.com/problems/asteroid-collision

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        final = []
        for a in asteroids:
            if(a > 0):
                final.append(a)
            elif(len(final) == 0 or final[-1] < 0):
                final.append(a)
            else:
                a_exploded = False
                while(len(final) > 0):
                    p = final.pop()
                    if(p < 0):
                        final.append(p)
                        final.append(a)
                        break
                    if(p > -a):
                        final.append(p)
                        break
                    elif(p == -a):
                        a_exploded = True
                        break
                if(len(final) == 0 and not a_exploded): final.append(a)
        return final
        