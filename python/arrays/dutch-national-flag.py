# Given an array of integers (0, 1, and 2 - 3 different values) Sort this array
# in linear running time using constant memory.

# Not able to use a data structure to hold the values
# [0, 1, 2, 1, 2, 0, 0] -> [0, 0, 0, 1, 1, 2, 2]

# Use a three-way partition
# Pivot value is always 1

def dutch_flag_problem(nums, pivot=1):
    i = 0
    j = 0
    k = len(nums) - 1

    while j <= k:
        # Current Element is 0
        if nums[j] < pivot:
            swap(nums, i, j)
            i += 1
            j += 1
        # Current Element is 2
        elif nums[j] > pivot:
            swap(nums, j, k)
            k -= 1
        # Current Element is 1
        else:
            j += 1
    return nums

def swap(nums, index1, index2):
    nums[index1], nums[index2] = nums[index2], nums[index1]

if __name__ == "__main__":
    print(dutch_flag_problem([1, 1, 0, 2]))
    print(dutch_flag_problem([0, 1, 2, 2, 1, 0, 0, 2, 2, 1]))