# Hash Table method - Create two hash tables whose keys should have the same values
# Time : O(n)
#Space : O(n) -- SInce two data structures (hashtables) created

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT 
    
# Last line same as below code : If a character is in the first hash table but not the second then return False
# for c in countS:
#   if countS[c] != countT.get(c, 0):
#       return False
# return True