// https://leetcode.com/problems/3sum-with-multiplicity

class Solution:
    def threeSumMulti(self, arr: [int], target: int) -> int:
        arr.sort()
        multiplicities = collections.Counter(arr)
        count = 0
        i = 0
        while(i < len(arr) - 2):
            j,k = i+1,len(arr)-1
            current_target = target - arr[i]
            while(j < k):
                current_sum = arr[j] + arr[k]
                if(current_sum < current_target):
                    j += 1
                elif(current_sum > current_target):
                    k -= 1
                else:
                    m_i = multiplicities[arr[i]]
                    m_j = multiplicities[arr[j]]
                    m_k = multiplicities[arr[k]]
                    reversed_perms = 1
                    if(arr[i] == arr[j]):
                        m_j -= 1
                        reversed_perms *= (reversed_perms + 1)
                    if(arr[j] == arr[k]):
                        m_k  = m_j - 1
                        reversed_perms *= (reversed_perms + 1)
                    count += m_i * m_j * m_k // reversed_perms
                    # print("count, arr[i], arr[j], arr[k]: {} {} {} {}".format(count,arr[i],arr[j],arr[k]) )
                    # print("multip   {}      {}      {}".format(m_i,m_j,m_k) )
                    # print("rev_perm {}".format(reversed_perms))
                    j += 1
                    k -= 1
                    while(j < k and arr[j] == arr[j-1]):
                        j += 1
                    while(j < k and arr[k] == arr[k+1]):
                        k -= 1
            i += 1
            while(i < len(arr) - 2 and arr[i] == arr[i-1]):
                i += 1
        return count % (10**9+7)