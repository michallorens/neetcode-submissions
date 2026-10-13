class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            key = "".join(sorted(s))

            if key in anagrams.keys():
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]

        return [v for v in anagrams.values()]
