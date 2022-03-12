class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        even = 1

        if (n1+n2) == 1:
            if n1==1:
                return nums1[0]
            else:
                return nums2[0]
        elif (n1+n2)%2 == 1:
            even = 0
        else:
            even = 1

        i1 = 0
        i2 = 0
        count = 0
        sum = 0
        temp = 0
        list = []
        print ((n1+n2)//2+1)
        while count < ((n1+n2)//2+1):
            if i2 == n2:
                list.append(nums1[i1])
                i1 = i1+1
            elif i1 == n1:
                list.append(nums2[i2])
                i2 = i2+1
                
            elif nums1[i1]>=nums2[i2]:
                list.append(nums2[i2])
                i2 = i2+1
            else:
                list.append(nums1[i1])
                i1 = i1+1
            count = count +1
        if even == 0:
            return list[count-1]
        else:
            return float(list[count-2]+list[count-1])/2