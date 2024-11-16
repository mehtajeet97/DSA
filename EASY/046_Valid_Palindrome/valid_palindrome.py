class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Create New String
        newStr =""
        #Check for each Character in Input String is Alphanumeric
        for c in s:
            if c.isalnum():
        #While adding make it lowercase
                newStr += c.lower()
        #Check whether new string and its reverse are the same
        return newStr == newStr[::-1]