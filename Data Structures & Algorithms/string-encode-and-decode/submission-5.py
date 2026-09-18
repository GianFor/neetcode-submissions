class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        sizes = ""
        for s in strs:
            sizes += str(len(s)) + ","
        
        out = sizes + "#"

        for s in strs:
            out += s

        return out

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        sizes = ""
        strings = ""
        numbers = True

        for c in s:
            if c != "#" and numbers:
                sizes += c
            elif c == "#" and numbers:
                numbers = False
            else:
                strings += c

        
        sizes = sizes.split(",")
        sizes.pop()
        current = 0
        res = []
        for size in sizes:
            res.append(strings[current:(current+int(size))])
            current += int(size)

        return res
