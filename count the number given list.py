def list_count(nums):
    count=0
    for num in nums:
        if num==5:
            count=count+1
    return count
print(list_count([1,2,4,5,6]))
print(list_count([1,4,5,4,7,4]))