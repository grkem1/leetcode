# https://leetcode.com/problems/open-the-lock

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if('0000' in deadends): return -1
        if(target == '0000'): return 0
        explored = set(['0000'])
        step = 1
        sweep = ['0000']
        while(len(sweep)>0):
            # print(len(sweep))
            next_sweep = []
            for number in sweep:
                for index,digit in enumerate(number):
                    new_digits = [chr((ord(digit)+1-48)%10+48)]
                    new_digits.append(chr((ord(digit)-1-48)%10+48))
                    # print(new_digits)
                    for d in new_digits:
                        new_number = number[:index]+d+number[index+1:]
                        # print(new_number)
                        if(new_number in deadends):continue
                        if(new_number not in explored):
                            if(new_number == target): return step
                            explored.add(new_number)
                            next_sweep.append(new_number)
            sweep = next_sweep
            step += 1
        return -1
