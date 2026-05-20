class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}
        for i in s:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1
        for j in t:
            if j in dictt:
                dictt[j] +=1
            else:
                dictt[j] = 1   
        return True if dicts == dictt else False              