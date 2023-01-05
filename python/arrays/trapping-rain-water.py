# Given n non-negative integers representing an elevation map where the 
# width of each bar is 1. Compute how much water it can trap after raining!

# Translated: Find the maximum amount of water that can be trapped within a
# given set of bars where each bar's width is 1 unit

#         x
#     x 1 x
# x 1 x 1 x
# x x x x x

# Input of: [2, 1, 3, 1, 4] -> x = bars
# Answer: 3 units (1)

# Base case - less than 3 bars (n < 3) can not trap any water
# Base case - the first and last bars can not trap any water 
# (no need to consider them)

# Base principle behind the algorithm:
# The amount of water trapped depends on the height of the boundary bars

# Find max bar height on left and then right based on the index position
# We must consider every item in O(N) linear running time, + for N times 
# we have to find the max values - takes O(N) linear running time

# Final run time: O(N^2)
# Can be reduced to O(N) by using dynamic programming (pre-compute)
from typing import List

def trapping_water_problem(heights: List[int]) -> int:
    if len(heights) < 3:
        return 0

    left_max = [0 for _ in range(len(heights))]
    right_max = [0 for _ in range(len(heights))]

    # Identify left max values (skip first)
    for i in range(1, len(heights)):
        left_max[i] = max(left_max[i - 1], heights[i - 1])

    # Identify right max values (skip last) - reverse iteration
    for i in range(len(heights) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i + 1])

    # Consider all the items in O(N) and sum up trapped rain water units
    trapped = 0
    # skip first and last bars
    for i in range(1, len(heights) - 1):
        if min(left_max[i], right_max[i]) > heights[i]:
            trapped += min(left_max[i], right_max[i]) - heights[i]

    return trapped

if __name__ == "__main__":
    print(trapping_water_problem([1, 2, 3, 4]))
    print(trapping_water_problem([1, 0, 2, 1, 3, 1, 2, 0, 3]))