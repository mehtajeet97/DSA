class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        # First pass: count the zeros to be duplicated
        zeros_to_duplicate = 0
    
        for i in range(n):
            if arr[i] == 0:
                zeros_to_duplicate += 1
    
        # Second pass: duplicate zeros from the back to the front
        for i in range(n - 1, -1, -1):
            if zeros_to_duplicate > 0:
                # Calculate new position of the element
                new_index = i + zeros_to_duplicate
                # If new index is within bounds, we need to shift the value
                if new_index < n:
                    arr[new_index] = arr[i]
                # If the current element is zero, we need to duplicate it
                if arr[i] == 0:
                    zeros_to_duplicate -= 1
                    if new_index - 1 < n:  # Ensure we don't go out of bounds
                        arr[new_index - 1] = 0