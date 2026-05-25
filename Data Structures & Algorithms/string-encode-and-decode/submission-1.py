class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        sizes = []
        for i in strs:
            sizes.append(len(i))
            sizes.append(",")
        for s in sizes:
            res += str(s)
        res += "#"
        for s in strs:
            res += s
        return res    
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes = []
        res = []
        i = 0
        num = ""
        while s[i] != "#":
            if s[i] == ",":
                sizes.append(int(num))
                num = ""
            else:
                num += s[i] 
            i += 1  
        i += 1    
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res             

