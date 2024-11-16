class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initiate pointers i, j, k from the end of arrays
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
        #Check for the greater number in two arrays and place it at the end
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # Check for any remaining elements in second array 
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1