class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        for ch in magazine:
            count[ch] = 1 + count.get(ch, 0)
        
        for cha in ransomNote:
            if cha not in count or count[cha] == 0:
                return False
            else:
                count[cha] -= 1
        
        return True