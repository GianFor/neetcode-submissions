class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out = out + s + "_._"
        
        return out

    def decode(self, s: str) -> List[str]:
        strs = s.split("_._")
        strs.pop()

        return strs