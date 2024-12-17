# https://leetcode.com/problems/construct-string-with-repeat-limit


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        l = len(s)
        s = collections.Counter(s)
        q = collections.deque((sorted([[key, s[key]] for key in s], reverse=True)))
        result = []
        repeated = ""
        count = 0
        while q:
            if q[0][0] == repeated:
                if count == repeatLimit:
                    if len(q) == 1:
                        break
                    result.append(q[1][0])
                    repeated = q[1][0]
                    count = 1
                    q[1][1] -= 1
                    if q[1][1] == 0:
                        del q[1]
                else:
                    result.append(q[0][0])
                    count += 1
                    q[0][1] -= 1
                    if q[0][1] == 0:
                        del q[0]
            else:
                result.append(q[0][0])
                q[0][1] -= 1
                repeated = q[0][0]
                count = 1
                if q[0][1] == 0:
                    del q[0]
        return "".join(result)
