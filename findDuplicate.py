# program to find duplicate element in n+1 size array. 
# No more than O(1) space. 

def findDuplicate(nums):
    # return (sum(nums)-sum(range(len(nums))))

    if len(nums) > 1:
        slow = nums[0]
        fast = nums[nums[0]]

        print("First loop")
        while fast != slow:
            print(f"Slow: {slow}, Fast:{fast}")
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        fast = 0
        print("Second loop")
        while fast != slow:
            print(f"Slow: {slow}, Fast:{fast}")
            slow = nums[slow]
            fast = nums[fast]
        return slow

    return -1

print(findDuplicate([1,3,4,2,2]))