class Solution:
    def makeGood(self, s: str) -> str:
        # Create stack
        stack = []
        i = 0
        # Iterate through input string
        while i<len(s):
        # Compare each element lowered with previous element lowered
            if ( 
                stack and
                stack[-1] != s[i] and
                stack[-1].lower() == s[i].lower()
                ):
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        # String Joining is simpler time than Concatenation
        return "".join(stack)