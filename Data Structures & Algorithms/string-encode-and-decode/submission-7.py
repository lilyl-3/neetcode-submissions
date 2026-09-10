class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        left, right = 0, len(s)-1 

        while left < right:
            i = left
            while s[i] != '#':
                i += 1
            w_len = int(s[left:i])
            res.append(s[i+1:i+1+w_len])
            left = i+1+w_len
        return res