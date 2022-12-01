nums = [int(el) for el in input().split()]
dup = [x for i, x in enumerate(nums) if i != nums.index(x)]
    
print(dup)
