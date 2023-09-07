class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        map = {}
        for letter in magazine:
            if letter.isalnum():
                if letter in map.keys():
                    map[letter] = map[letter] + 1
                else:
                    map[letter] = 1
        for letter in ransomNote:
            if letter.isalnum():
                if letter in map.keys() and map[letter] > 0:
                    map[letter] = map[letter] - 1
                else:
                    return False
        return True
