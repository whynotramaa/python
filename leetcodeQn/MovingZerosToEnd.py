def moveZeros(nums):
    nums[:] = [num for num in nums if num!=0] + [0]*nums.count(0)
    return nums

print(moveZeros([1,2,0,0,3,4,0]))