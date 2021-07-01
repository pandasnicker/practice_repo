import math

def findMedianSortedArrays(nums1, nums2) -> float:
    nums3 = sorted(nums1.extend(nums2))
    print(nums3)
    if len(nums3)%2 == 0:
        return nums3[len(nums3)/2]
    else:
        return (nums3[math.floor(len(nums3)/2)] + nums3[math.floor(len(nums3)/2)+1])/2

 

nums1 = [','.join(int(item) for item in input("Enter sorted Array 1 : ").split())]
nums2 = [','.join(int(item) for item in input("Enter sorted Array 2 : ").split())]

# nums1 = [1,3]
# nums2 = [2]

print(' '.join(map(str,nums1)))
print(' '.join(map(str,nums2)))

print(findMedianSortedArrays(nums1, nums2))