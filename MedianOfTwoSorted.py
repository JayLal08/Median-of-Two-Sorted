class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
       nums1 = [1,3]
       nums2 = [2]

    def Solution(arr):

      m = len(nums1)
      n = len(nums2)

    if m%2 == 0:
         z = m // 2
         a = arr[z]
         b = arr[z+1]
         ans = (a + b)/2
         return ans

    if n%2 != 0:
         z = n+1
         a = arr[z]
         ans = a / 2
         return ans

self = nums1 + nums2

print(Solution(self))