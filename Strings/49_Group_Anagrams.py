from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for each in strs:
            k = ''.join(sorted(each)) 
            groups[k].append(each)
        return list(groups.values())
