class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        t_list = list(t)

        for i in range(len(s)):
            for j in range(len(t_list)):
                if s[i] == t_list[j]:
                    t_list.pop(j)
                    break  
                    
        return len(t_list) == 0





        """
        given two strings
      s = "hello"
      t = "olleh"
      if theyre both anagrams of eachother return TRUE
      otherwise return false

"""