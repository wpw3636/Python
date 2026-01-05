def removeDuplicates(nums):
    k = 0
    for n in range(nums[0], nums[-1]+1):
        amt = nums.count(n)
        if amt == 0:
            pass
        elif amt == 1:
            k += 1
        else:
            k += 1
            while amt > 1:
                nums.remove(n)
                amt -= 1
    return nums
nums = [1,1,1,2,4,4,5,5,5,6] #Enter a list of increasing integers and the program will remove all duplicates and returnt he list
print(removeDuplicates(nums))