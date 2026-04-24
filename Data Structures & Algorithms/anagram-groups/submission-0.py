class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ana_dict = {}

        for i in strs:
            word = "".join(sorted(i))
            if word not in ana_dict:
                ana_dict[word] = [i] 
            else:
                ana_dict[word].append(i)
        
        return list(ana_dict.values())
