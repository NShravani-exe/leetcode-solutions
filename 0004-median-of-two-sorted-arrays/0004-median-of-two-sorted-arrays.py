class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        low, high = 0, len(A)
        
        while low <= high:
            part_A = (low + high) // 2
            part_B = half - part_A
            
            A_left = A[part_A - 1] if part_A > 0 else float('-inf')
            A_right = A[part_A] if part_A < len(A) else float('inf')
            
            B_left = B[part_B - 1] if part_B > 0 else float('-inf')
            B_right = B[part_B] if part_B < len(B) else float('inf')

            if A_left <= B_right and B_left <= A_right:
                if total % 2 != 0:
                    return float(min(A_right, B_right))
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            
            elif A_left > B_right:
                high = part_A - 1
            else:
                low = part_A + 1
        