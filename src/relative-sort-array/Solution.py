# https://leetcode.com/problems/relative-sort-array

class Solution:
    def relativeSortArray(self, arr1: [int], arr2: [int]) -> [int]:
        d = dict()
        for i, el in enumerate(arr2):
            d[el] = i

        def k(x):
            nonlocal d
            if(x in d):
                return d[x]
            else:
                return x + 1000

        return sorted(arr1, key=k)


if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    s = Solution()
    print(s.relativeSortArray(arr1, arr2))
