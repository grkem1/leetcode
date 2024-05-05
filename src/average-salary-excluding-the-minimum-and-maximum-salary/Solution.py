// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary

class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        smallest = 10**6
        largest = 1
        for el in salary:
            total += el
            smallest = min(el,smallest)
            largest = max(el,largest)
        return (total - smallest - largest) / (len(salary)-2)