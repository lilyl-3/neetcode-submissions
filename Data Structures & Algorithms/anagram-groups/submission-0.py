class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key is sorted anagram
        # values are list of anagrams 
        anagramList = defaultdict(list)

        for s in strs:
            sortedWord = ''.join(sorted(s))
            anagramList[sortedWord].append(s)

        return list(anagramList.values())
