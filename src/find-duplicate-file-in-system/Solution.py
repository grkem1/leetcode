// https://leetcode.com/problems/find-duplicate-file-in-system

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicate_content_set = set()
        content_file_dict = dict()
        for p in paths:
            folder,*files = p.split()
            for f in files:
                file,content = f.split(".txt")
                if(content in content_file_dict):
                    duplicate_content_set.add(content)
                    content_file_dict[content].append(folder + "/" + file + ".txt")
                else:
                    content_file_dict[content] = [folder + "/" + file + ".txt"]
        return([content_file_dict[d] for d in duplicate_content_set])