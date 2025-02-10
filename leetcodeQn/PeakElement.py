
def findPeakElement(nums):
        if (len(nums)) == 1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1

        low,high = 1, len(nums)-2
        while(low<=high):
            mid = (low+high)//2
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]>nums[mid-1]:
                low = mid+1
            else:
                high = mid-1
        return -1
        

print(findPeakElement([1,2,3,4,5,6,4,2,1]))

# returns index and not exactly the element 