def findMaxConsecutiveOnes(nums):
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 0
        return max(count, max_count)

print(findMaxConsecutiveOnes([1,0,0,0,1,1,1,1,1,0,0]))