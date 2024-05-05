// https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options

class Solution:
    def countOrders(self, n: int) -> int:
        # new_perms = [1]
        # for i in range(1,n):
            # new_perms.append(new_perms[-1]+4*i+1)
        # total_perms = 1
        # for n in new_perms:
            # total_perms *= n
        # print(new_perms)
        # return total_perms % (10**9+7)
        perms = 1
        last = 0
        for i in range(n):
            last += 4*i+1
            perms *= last
        return perms % (10**9+7)