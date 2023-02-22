# Chloe Ogles

import numpy as np

def nevilles_method(x_points, y_points, x):
    matrix = np.zeros((3,3))
    for counter, row in enumerate(matrix):
        row[0] = y_points[counter]
    num_of_points = len (x_points)
    for i in range(1, num_of_points):
        
        for j in range(1,i+1):
            
            first_multi = (x - x_points[i-j]) * matrix[i][j-1]
            second_multi = (x - x_points[i]) * matrix[i-1][j-1]
            denominator = x_points[i] - x_points[i-j]
            coefficient = (first_multi - second_multi)/denominator
            matrix[i][j] = coefficient
            
    print(matrix[len(x_points)-1][len(x_points)-1])
    
    return matrix

def divided_difference_table(x_points, y_points):
    size: int = len(x_points)
        
    matrix: np.array = np.zeros((4,4))
    for index, row in enumerate(matrix):
        
        row[0] = y_points[index]
    for i in range(1, size):
        
        for j in range(1, i+1):
            num = matrix[i][j-1] - matrix[i-1][j-1]
            denom = x_points[i] - x_points[i-j]
            operation = num / denom
            matrix[i][j] = (operation)
    return matrix

def get_approximate_result(matrix, x_points, value): 
    reoccuring_x_span = 1
    reoccuring_px_result = matrix[0][0]
    
    for index in range(1, len(x_points)):
        polynomial_coefficient = matrix[index][index]
        reoccuring_x_span *= (value - x_points[index-1])
        
        mult_operation = polynomial_coefficient * reoccuring_x_span
        reoccuring_px_result += mult_operation
    
    return reoccuring_px_result

np.set_printoptions(precision=7, suppress=True, linewidth=100
                   )
def apply_div_dif(matrix: np.array):
    size = len(matrix)
    for i in range(2, size):
        for j in range(2, i+2):
            if j >= len(matrix[i]) or matrix[i][j] != 0:
                continue
            
            left: float = matrix[i][j-1]
            diagonal_left: float = matrix[i-1][j-1]
            numerator: float = ( left - diagonal_left )
            denominator = matrix[i][0]- matrix[i-j+1][0]
            operation = numerator / denominator
            matrix[i][j] = operation
    
    return matrix

def hermite_interpolation():
    x_points = [3.6, 3.8, 3.9]
    y_points = [1.675, 1.436, 1.318]
    slopes = [-1.195, -1.188, -1.182]
    num_of_points = 2*len(x_points)
    matrix = np.zeros((num_of_points, num_of_points))
    counter = 0
    for x in range(0, num_of_points,2):
        matrix[x][0] = x_points[counter]
        matrix[x+1][0] = x_points[counter]
        counter +=1
    counter = 0
    for x in range(0,num_of_points, 2):
        matrix[x][1] = y_points[counter]
        matrix[x+1][1] = y_points[counter]
        counter +=1
     
    counter = 0
    for x in range(1,num_of_points,2):
        matrix[x][2] = slopes[counter]
        counter +=1
    
    filled_matrix = apply_div_dif(matrix)
    print(filled_matrix)

def CubicSplineInterpolation ():
    
    x_points = np.array([2, 5, 8, 10])
    y_points = np.array([3, 5, 7, 9])

    size = len(x_points)

    Matrix = np.zeros((size, size))
    Matrix[0, 0] = 1
    Matrix[size-1, size-1] = 1
    
    for i in range(1, size-1):
        Matrix[i, i-1] = x_points[i] - x_points[i-1]
        Matrix[i, i] = 2 * (x_points[i+1] - x_points[i-1])
        Matrix[i, i+1] = x_points[i+1] - x_points[i]

    Array = np.zeros(size)
    
    for i in range(1, size-1):
        Array[i] = 3 * (y_points[i+1] - y_points[i]) / (x_points[i+1] - x_points[i]) - \
        3 * (y_points[i] - y_points[i-1]) / (x_points[i] - x_points[i-1])

    XArray = np.linalg.solve(Matrix, Array)
    
    print(Matrix)
    print("\n")
    print(Array)
    print("\n")
    print(XArray)
    
if __name__ == "__main__":
    
    x_points = [3.6, 3.8, 3.9]
    y_points = [1.675, 1.436, 1.318]
    approximating_value = 3.7
    
    nevilles_method(x_points, y_points, approximating_value)
    print("\n")
    
    x_points = [7.2, 7.4, 7.5, 7.6]
    y_points = [23.5492, 25.3913, 26.8224, 27.4589]
    divided_table = divided_difference_table(x_points, y_points)
    
    approximating_x = 7.3
    final_approximation = get_approximate_result(divided_table, x_points, approximating_x)
    
    AnswerArray = []
    for i in range(1, len(x_points)):
        AnswerArray.append(divided_table[i][i])

    print(AnswerArray)
    print("\n")
    print(final_approximation)
    print("\n")
    hermite_interpolation()
    print("\n")
    CubicSplineInterpolation()
