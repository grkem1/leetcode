# https://leetcode.com/problems/consecutive-characters

class Solution:
    def maxPower(self, s: str) -> int:
        power = 0
        max_power = 0
        last_char = '#'
        for char in s:
            if char != last_char:
                max_power = max(power,max_power)
                power = 1
                last_char = char
            else:
                power += 1
        max_power = max(max_power,power)
        return max_power