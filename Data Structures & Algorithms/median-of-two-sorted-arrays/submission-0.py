class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Need to look at what the middle number is for each list
        # This will then give an indication of where the middle of the array should be
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2

        while True:
            m_A = (l + r) // 2
            m_B = half - m_A - 2

            A_left = A[m_A] if m_A >= 0 else float("-infinity")
            A_right = A[m_A + 1] if (m_A + 1) < len(A) else float("infinity")
            B_left = B[m_B] if m_B >= 0 else float("-infinity")
            B_right = B[m_B + 1] if (m_B + 1) < len(B) else float("infinity")

            if A_left <= B_right and B_left <= A_right:
                if total % 2:
                    return min(A_right, B_right)
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = m_A - 1
            else:
                l = m_A + 1