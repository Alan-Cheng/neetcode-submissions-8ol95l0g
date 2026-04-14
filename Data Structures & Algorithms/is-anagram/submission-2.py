class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if m != n:
            return False

        h_map = {}

        for i in range(n):
            if not h_map.get(s[i]):
                h_map[s[i]] = 1
            else:
                h_map[s[i]] += 1
        
        for j in range(m):
            if h_map.get(t[j]) == 0 or t[j] not in h_map:
                return False
            else:
                h_map[t[j]] -= 1
        
        return True