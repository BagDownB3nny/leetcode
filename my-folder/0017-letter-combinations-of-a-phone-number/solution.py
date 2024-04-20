class Solution:
    
    def letterCombinations(self, digits):
        """
        :type s: str
        :rtype: int
        """
        
        letterSets = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        };
            
        
        def helper(s):
            if s == "":
                return []
            elif len(s) == 1:
                newWords = []
                for letter in letterSets[s]:
                    newWords.append([letter])
                return newWords
            digit = s[-1]
            words = helper(s[:-1])
            newWords = []
            for word in words:
                for letter in letterSets[digit]:
                    newWord = word.copy()
                    newWord.append(letter)
                    newWords.append(newWord)
            return newWords
                    
        words = helper(digits)
        if len(words) < 0:
            return []
        ans = []
        for word in words:
            ans.append(''.join(word))
        return ans

