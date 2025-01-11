def missingNumber(nums):
        n = len(nums)
        sum_all = (n*(n+1))/2
        for num in nums:
            loop_sum = sum(nums)
        return int(sum_all - loop_sum)

print(missingNumber([1,2,3,4,5,7,8,9,0]))