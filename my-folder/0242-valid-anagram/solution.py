class Solution(object):
    def isAnagram(self, s, t):
        letters_dict = {}
        for letter in s:
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1
        for letter in t:
            if letter in letters_dict:
                if letters_dict[letter] == 1:
                    letters_dict.pop(letter)
                else:
                    letters_dict[letter] -= 1
            else:
                return False
        return len(letters_dict) == 0
        
        
