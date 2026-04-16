class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
U:   find the repeated number in the array
    - boolean answer, return true if yes, false if not
    - What if the values are negative
    - what is the fast way to solve it

M:  Algos to use
- brute force: loop through the array twice
    if a value has been seen before we compare current one array vs the other, if not continue going through the entire array

- easiest way is to build a dictionary(freq map)
    create keys by looping through the given array, and if a value is its count is added by +1

P:  we loop through our array, we then loop through a second time to see if any values are the same assume False before proving True

        """
        seen = set()
        for i in nums:
         if i in seen:
             return True
         seen.add(i)
        return False