# https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        new_path = []
        for p in path:
            if(p in ('.','')):
                continue
            if(p == ".."):
                if(len(new_path) > 0):
                    new_path.pop()
            else:
                new_path.append(p)
        return '/'+'/'.join(new_path)