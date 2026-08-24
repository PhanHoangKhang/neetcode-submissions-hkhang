class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []

        for n1 in nums1:
            arr.append(n1)

        for n2 in nums2:
            arr.append(n2)

        arr.sort()

        n = len(arr)

        mid = n // 2

        if n % 2 != 0:
            return float(arr[mid])
        else:
            return (arr[mid - 1] + arr[mid]) / 2

