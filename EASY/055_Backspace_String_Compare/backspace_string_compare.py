class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Create helper function to find the next valid character 
        # by skipping backspaces
        def nextValid(str, index):
            backspace = 0
            while index >= 0:
                if backspace == 0 and str[index] != "#":
                    break
                elif str[index] == '#':
                    backspace += 1
                else:
                    backspace -= 1
                index -= 1
            return index
        # Iterate from the end of both strings
        # using the helper to identify valid characters
        indexS, indexT = len(s)-1, len(t)-1
        while indexS >= 0 or indexT >= 0:
            indexS = nextValid(s, indexS)
            indexT = nextValid(t, indexT)

            charS = s[indexS] if indexS>=0 else ""
            charT = t[indexT] if indexT>=0 else ""
        # Compare valid characters from both strings
        # if mismatch is found, return False
            if charS != charT:
                return False
            indexS -= 1
            indexT -= 1
        # If all valid characters match, return True
        return True