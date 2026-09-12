class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ 
        Input:  s and t - > strings e.g "hello", "good-bye"...

        Output: Bool True or False

        ? What is an anagram: A word that uses the same chars as another word
        e.g "racecar", "carrace"
            Bool - > True

        DSA:    

        - Brute force: con might take too much mem if input is too long
        - Dictionary: Have the individual chars be the key
            'h': count
         """

        if len(s) != len(t):
            return False

        ana_s,ana_t = {}, {}

        for i, char in enumerate(s):
            if char in ana_s:
                ana_s[char] += 1
            else:
                ana_s[char] = 1

        for i, char in enumerate(t):
            if char in ana_t:
                ana_t[char] += 1
            else:
                ana_t[char] = 1

        if ana_s.items() == ana_t.items():
            return True
        else:
            return False




