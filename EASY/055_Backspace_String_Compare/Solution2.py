# Not Optimum as space utilized for stack creation

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Create Helper Function
        def str2stack(string):
        # Create Stack
            stack = []
            for char in string:
        # Add nonbackspace character, push into stack
                if char != '#':
                    stack.append(char)
        # For backspace character, pop out of stack
                elif stack:
                    stack.pop()
            return stack
        
        # Compare if equal
        return str2stack(s) == str2stack(t)