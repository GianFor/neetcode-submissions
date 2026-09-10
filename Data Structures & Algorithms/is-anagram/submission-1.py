class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars1 = {}
        chars2 = {}
        
        for c in s:
            if chars1.get(c) is None:
                chars1[c] = 1
            else:
                chars1[c] += 1

        for c in t:
            if chars2.get(c) is None:
                chars2[c] = 1
            else:
                chars2[c] += 1
        
        return chars1 == chars2