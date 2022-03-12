class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Sorted nums1 and nums2
        # sorted the largest at the end index of nums1
        if m == 0:
            nums1[:] = nums2[:]
        elif n != 0:
            i1, i2 = m-1, n-1
            for i in range(len(nums1)-1, -1, -1):
                if i1 <0 :
                    nums1[i] = nums2[i2]
                    i2 -= 1
                elif i2 <0 or nums1[i1] >= nums2[i2]:
                    nums1[i] = nums1[i1]
                    i1 -= 1
                else:
                    nums1[i] = nums2[i2]
                    i2 -= 1