'''
Program to list out pairs of indices of an input array which adds to a target number
'''

def pairs(nums, target):
    res = []
    for count, value in enumerate(nums,0):
        other_num = target - value
        if other_num in nums and nums.index(other_num) != count:
            res.append((count,nums.index(other_num))) if tuple(sorted((count, nums.index(other_num)))) not in res else None
            # print(tuple(sorted((count, nums.index(other_num)))))
    
    return res

print(pairs([1,2,3,4,5,6,7,9], 15))

