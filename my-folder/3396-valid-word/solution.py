class Solution:
    def isValid(self, word: str) -> bool:
        consonents = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
        upperC = [i.upper() for i in consonents]
        vowels = ["e","u","i","o","a"]
        upperV = [i.upper() for i in vowels]
        nums = [str(i) for i in range(10)]
        
        q = False
        w = False
        if len(word) < 3:
            return False
        for i in range(len(word)):
            if word[i] not in consonents and word[i] not in vowels and word[i] not in nums and word[i] not in upperC and word[i] not in upperV:
                return False
            if word[i] in consonents or word[i] in upperC:
                q = True
            if word[i] in vowels or word[i] in upperV:
                w = True
        return q and w
