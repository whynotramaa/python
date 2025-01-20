def rearrangeArray(nums):
       arr = [0] * len(nums)
       posindex,negindex=0,1
       for i in range (0, len(nums)):
           if nums[i] > 0:
               arr[posindex] = nums[i]
               posindex+=2
           else:
               arr[negindex] = nums[i]
               negindex+=2
       return arr

print(rearrangeArray([2,-3,1,2,2,4,5,6,-2,-2,2-2,-4,-3,-5]))