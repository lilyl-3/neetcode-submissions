class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        list = []

        for char in s:
            list.append(char)

        for char in t:
            if char in list:
                list.remove(char)
            else:
                return False

        return len(list) == 0
        