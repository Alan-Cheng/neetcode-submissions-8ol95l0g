class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        
        for i, s in enumerate(strs):
            sorted_s = "".join(sorted(s))
            if sorted_s not in mapping:
                mapping[sorted_s] = [i]
            else:
                mapping[sorted_s].append(i)
        
        output = []
        for sorted_s, idxs in mapping.items():
            group = []
            for idx in idxs:
                group.append(strs[idx])
            output.append(group)
        
        return output
            