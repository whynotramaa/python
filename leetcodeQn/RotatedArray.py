def rotate(nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if k==0:
            return
        nums1 = nums[-k:] #--> last sa how many
        nums2 = nums[:-k] #--> upto how much ?
        nums[:] = nums1 + nums2
        return nums
print(rotate([1,2,3,4,5,6,7], 3))