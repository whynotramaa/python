def checl(nums):
        count = 0
        for i in range (1, len(nums)):       
            if nums[i] >= nums[i-1]:
                continue
            else:
                count = count + 1           
        if nums[-1] > nums[0]:
            count = count + 1

        return count<=1

print(checl([2,1,3,4]))