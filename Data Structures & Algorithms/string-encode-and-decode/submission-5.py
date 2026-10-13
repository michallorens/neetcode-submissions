class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        
        for s in strs:
            result = result + s + chr(257)

        return result

    def decode(self, s: str) -> List[str]:
        return s.split(chr(257))[:-1]
