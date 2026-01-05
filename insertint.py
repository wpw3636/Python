def searchInsert(nums, target):
    for n in nums:
        if n >= target:
            return nums.index(n)
            break
    else:
        return nums.index(nums[-1]) + 1
nums = [1,3,7,8,12]
target = 5
print(searchInsert(nums, target))