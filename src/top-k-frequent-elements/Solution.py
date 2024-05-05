// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = collections.Counter(nums)
        topK = [el[0] for el in elements.most_common(k)]
        return topK