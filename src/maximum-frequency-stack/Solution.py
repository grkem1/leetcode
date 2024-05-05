// https://leetcode.com/problems/maximum-frequency-stack

class FreqStack:

    def __init__(self):
        self.number_freq = collections.defaultdict(int)
        self.freq_number = collections.defaultdict(lambda: collections.defaultdict(int))

    def push(self, val: int) -> None:
        freq = self.number_freq[val]
        self.number_freq[val]+=1
        self.freq_number[freq+1][val] = val

    def pop(self) -> int:
        # print(self.freq_number)
        most_frequents = self.freq_number.popitem()
        while(len(most_frequents) < 2 or len(most_frequents[1]) == 0):
            most_frequents = self.freq_number.popitem()
        val = most_frequents[1].popitem()[0]
        self.freq_number[most_frequents[0]] = most_frequents[1]
        freq = self.number_freq[val]
        self.number_freq[val]-=1
        if(self.number_freq[val]==0):del(self.number_freq[val])
        return val
