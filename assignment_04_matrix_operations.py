# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols, name="Matrix"):
    print(f"\nEntering values for {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"  Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    for row in matrix:
        for val in row:
            print(f"{val:4d}", end=" ")
        print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
            
    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
   
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
                
    return result


def main():
    print("=" * 60)
    print("PART A: TRANSPOSE A MATRIX")
    print("=" * 60)
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    
    mat_a = read_matrix(m, n, "Original Matrix")
    
    print("\nOriginal Matrix:")
    display_matrix(mat_a)
    
    mat_transposed = transpose_matrix(mat_a)
    print("\nTransposed Matrix:")
    display_matrix(mat_transposed)

    print("\n" + "=" * 60)
    print("PART B: ADD TWO MATRICES")
    print("=" * 60)
    m = int(input("Enter number of rows for both matrices: "))
    n = int(input("Enter number of columns for both matrices: "))
    
    mat_b1 = read_matrix(m, n, "Matrix 1")
    mat_b2 = read_matrix(m, n, "Matrix 2")
    
    mat_sum = add_matrices(mat_b1, mat_b2)
    print("\nSum of Matrices:")
    display_matrix(mat_sum)

    print("\n" + "=" * 60)
    print("PART C: MULTIPLY TWO MATRICES")
    print("=" * 60)
    m = int(input("Enter rows for Matrix A (M): "))
    n = int(input("Enter columns for Matrix A / rows for Matrix B (N): "))
    p = int(input("Enter columns for Matrix B (P): "))
    
    mat_c1 = read_matrix(m, n, "Matrix A")
    mat_c2 = read_matrix(n, p, "Matrix B")
    
    mat_product = multiply_matrices(mat_c1, mat_c2)
    print("\nProduct (A x B):")
    display_matrix(mat_product)


if __name__ == "__main__":
    main()