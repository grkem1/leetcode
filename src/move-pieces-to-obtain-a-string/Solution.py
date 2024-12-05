# https://leetcode.com/problems/move-pieces-to-obtain-a-string


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        R_count = 0
        L_count = 0
        for i in range(len(start)):
            if R_count > 0 and target[i] == "L" or L_count > 0 and target[i] == "R":
                return False
            if start[i] == target[i]:
                continue
            if (
                start[i] == "R"
                and target[i] == "L"
                or start[i] == "L"
                and target[i] == "R"
            ):
                return False
            if start[i] == "L" and target[i] == "_":
                if L_count > 0 and R_count == 0:
                    L_count -= 1
                else:
                    return False
            if start[i] == "R" and target[i] == "_":
                R_count += 1
            if start[i] == "_" and target[i] == "L":
                L_count += 1
            if start[i] == "_" and target[i] == "R":
                if R_count > 0 and L_count == 0:
                    R_count -= 1
                else:
                    return False
            # print(L_count, R_count)
        return L_count == R_count == 0
