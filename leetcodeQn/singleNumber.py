def singleNumber(nums):
        for num in nums:
            if nums.count(num) == 1:
                return num
                
print(singleNumber([1,2,1,2,3,4,3,5,5,5,5,6,6,7]))