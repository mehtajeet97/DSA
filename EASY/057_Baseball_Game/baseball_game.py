from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Create a stack 
        stack = []
        # Perform operations whil iterating through the input array
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])

            elif op == 'C':
                stack.pop()

            elif op == 'D':
                stack.append(2 * stack[-1])

            else:
                stack.append(int(op))
        # Return Sum of the Stack
        return sum(stack)