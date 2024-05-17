# https://leetcode.com/problems/unique-email-addresses

class Solution:
    def numUniqueEmails(self, emails: [str]) -> int:
        s = set()
        for e in emails:
            e = e.split('@')
            local = e[0].split('+')[0]
            local = ''.join(local.split('.'))
#            print(local,e[1])
            s.add((local,e[1]))
        return len(s)
