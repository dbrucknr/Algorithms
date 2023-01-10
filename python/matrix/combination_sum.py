def find_greatest_combination_sum(matrix):
    """
        This function first initializes the greatest_sum variable to the value
        of the first element in the matrix. It then iterates over each element 
        in the matrix and checks the combination sum of the current element 
        with the element above it (if it exists) and with the element to the 
        left of it (if it exists). If either of these combination sums is 
        greater than the current value of greatest_sum, greatest_sum is updated 
        to the new value.
    """
    # Initialize the greatest sum to the value of the first element in the matrix
    greatest_sum = matrix[0][0]
    
    # Iterate over each element in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Check the combination sum of the current element with the element above it (if it exists)
            if i > 0:
                current_sum = matrix[i][j] + matrix[i-1][j]
                if current_sum > greatest_sum:
                    greatest_sum = current_sum
            # Check the combination sum of the current element with the element to the left of it (if it exists)
            if j > 0:
                current_sum = matrix[i][j] + matrix[i][j-1]
                if current_sum > greatest_sum:
                    greatest_sum = current_sum
    return greatest_sum

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
greatest_sum = find_greatest_combination_sum(matrix)
print(greatest_sum)  # Output: 16 (from the combination 7+8+9)