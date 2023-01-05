def find_max_path(matrix):
    # Calculate size of matrix
    N = len(matrix)
    M = len(matrix[0])

    for outer_index in range(1, N):
        response = -1
        print("outer_index value:", matrix[outer_index])
        for inner_index in range(M):
            print("inner_index value:", matrix[outer_index][inner_index])
            # While all paths are possible, build sum
            if (inner_index > 0 and inner_index < M - 1):
                matrix[outer_index][inner_index] += max(matrix[outer_index - 1][inner_index],
                                                        max(matrix[outer_index - 1][inner_index - 1],
                                                            matrix[outer_index - 1][inner_index + 1]))
                print("All paths possible")
                print(matrix[outer_index][inner_index], response)

            elif (inner_index > 0):
                matrix[outer_index][inner_index] += max(
                    matrix[outer_index - 1][inner_index],
                    matrix[outer_index - 1][inner_index - 1]
                )
                print("Diagonal right is not possible")
                print(matrix[outer_index][inner_index], response)

            elif (inner_index < M - 1):
                matrix[outer_index][inner_index] += max(
                    matrix[outer_index - 1][inner_index],
                    matrix[outer_index - 1][inner_index + 1]
                )
                print("Diagonal left is not possible")
                print(matrix[outer_index][inner_index], response)

            print("Completed analysis, finding max from this:",
                  matrix[outer_index][inner_index], response)

            # Keep track of values over time - always set / select max
            response = max(matrix[outer_index][inner_index], response)
    return response


matrix = ([[10, 10, 2, 0, 20, 4],
           [1, 0, 0, 30, 2, 5],
           [0, 10, 4, 0, 2, 0],
           [1, 0, 2, 20, 0, 4]])

print(find_max_path(matrix))

def find_max_path_simple(matrix):
    max_sum = 0
    for row in matrix:
        row_max_sum = 0
        for element in row:
            row_max_sum = max(row_max_sum, element + max_sum)
        max_sum = max(max_sum, row_max_sum)
    return max_sum
