import numpy as np
import os
from dominant_eigen_value import power_method

# Clear Screen
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def mainMenu():
    
    clear()
    
    print(r"""
__  __       _        _                             _                    
|  \/  |     | |      (_)          /\               | |                   
| \  / | __ _| |_ _ __ ___  __    /  \   _ __   __ _| |_   _ _______ _ __ 
| |\/| |/ _` | __| '__| \ \/ /   / /\ \ | '_ \ / _` | | | | |_  / _ \ '__|
| |  | | (_| | |_| |  | |>  <   / ____ \| | | | (_| | | |_| |/ /  __/ |   
|_|  |_|\__,_|\__|_|  |_/_/\_\ /_/    \_\_| |_|\__,_|_|\__, /___\___|_|   
                                                        __/ |             
                                                        |___/              
""")

    print("1. Check Diagonalizability")
    print("2. Perform LU Decomposition")
    print("3. Find Dominant Eigenvalue")
    print("4. Singular Value Decomposition (SVD)")
    print("5. Exit")

    while True:
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            isDiagonalizable() 
            break
        elif choice == "2":
            LUDecomposition()
            break
        elif choice == "3":
            dominantEigenvalue()
            break
        elif choice == "4":
            svd()
            break
        elif choice == "5":
            print("\nExiting Matrix Analyzer Tool. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")

# For Matrix Input (Non-Square for SVD)
def input_matrix():
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            break
        except ValueError:
            print("Please enter valid integers for rows and columns.\n")

    print("\nEnter the matrix values row by row (separated by spaces):")
    matrix = []

    for i in range(rows):
        while True:
            row_input = input(f"Row {i + 1}: ").split()

            # Check if number of entries matches 'cols'
            if len(row_input) != cols:
                print(f"Row {i + 1} must have exactly {cols} entries. Try again.")
                continue

            try:
                # Convert all entries to float
                row = [float(x) for x in row_input]
                matrix.append(row)
                break  # valid row -> go to next
            except ValueError:
                print(f"Row {i + 1} contains non-numeric values. Try again.")

    return matrix

# FOr Matrix Input (Square Matrix)
def input_squareMatrix():
    while True:
        try:
            n = int(input("Enter the size of the square matrix (n x n): "))
            if n <= 0:
                print("Matrix size must be a positive integer.\n")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the matrix size.\n")

    print(f"\nEnter the {n}x{n} matrix values row by row (separated by spaces):")
    matrix = []

    for i in range(n):
        while True:
            row_input = input(f"Row {i + 1}: ").split()

            # Check if number of entries matches 'n'
            if len(row_input) != n:
                print(f"Row {i + 1} must have exactly {n} entries. Try again.")
                continue

            try:
                # Convert entries to float
                row = [float(x) for x in row_input]
                matrix.append(row)
                break  # valid row
            except ValueError:
                print(f"Row {i + 1} contains non-numeric values. Try again.")

    return matrix

def isDiagonalizable():
    clear()
    print(r"""
___  _                         _ _         _    _    ___ 
|   \(_)__ _ __ _ ___ _ _  __ _| (_)_____ _| |__| |__|__ \
| |) | / _` / _` / _ \ ' \/ _` | | |_ / _` | '_ \ / -_)/_/
|___/|_\__,_\__, \___/_||_\__,_|_|_/__\__,_|_.__/_\___(_) 
            |___/                                         
""")

    matrix = input_squareMatrix()
    n = len(matrix)
    A = np.array(matrix, dtype=float)
    
    eigvals, eigvecs = np.linalg.eig(A)
    
    rank = np.linalg.matrix_rank(eigvecs)

    unique_eigs = np.unique(np.round(eigvals, 6))
    diagonalizable = True

    for eig in unique_eigs:
        algebraic_mult = np.sum(np.isclose(eigvals, eig))

        B = A - eig * np.eye(n)
        geometric_mult = n - np.linalg.matrix_rank(B)

        if geometric_mult < algebraic_mult:
            diagonalizable = False


    print("\nEigenvalues:")
    print(np.round(eigvals, 4))

    print("\nEigenvectors:")
    print(np.round(eigvecs, 4))

    if diagonalizable:
        print("\nMatrix IS diagonalizable!")
    else:
        print("\nMatrix is NOT diagonalizable.")
    
    print()
    print("Press Enter to go back to main menu...")
    input()
    mainMenu()

def LUDecomposition():
    clear()
    print(r"""
__   __  __  ___                                   _ __  _         
/ /  / / / / / _ \___ _______  __ _  ___  ___  ___ (_) /_(_)__  ___ 
/ /__/ /_/ / / // / -_) __/ _ \/  ' \/ _ \/ _ \(_-</ / __/ / _ \/ _ \
/____/\____/ /____/\__/\__/\___/_/_/_/ .__/\___/___/_/\__/_/\___/_//_/
                                    /_/                                
""")


    matrix = input_squareMatrix()
    n = len(matrix)

    lower = [[0.0 for _ in range(n)] for _ in range(n)]
    upper = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        # Upper Triangular
        for k in range(i, n):
            temp_sum = sum(lower[i][j] * upper[j][k] for j in range(i))
            upper[i][k] = matrix[i][k] - temp_sum

        # Lower Triangular
        for k in range(i, n):
            if i == k:
                lower[i][i] = 1.0
            else:
                temp_sum = sum(lower[k][j] * upper[j][i] for j in range(i))
                if upper[i][i] == 0:
                    print("Matrix is singular — cannot perform LU decomposition.")
                    print()
                    print("Press Enter to go back to main menu...")
                    input()
                    mainMenu()
                lower[k][i] = (matrix[k][i] - temp_sum) / upper[i][i]

    print("\nLower Triangular Matrix:")
    for row in lower:
        print([f"{x:.2f}" for x in row])
        
    print("\nUpper Triangular Matrix:")
    for row in upper:
        print([f"{x:.2f}" for x in row])
        
    print()
    print("Press Enter to go back to main menu...")
    input()
    mainMenu()

def dominantEigenvalue():
    clear()
    print(r"""
___             _                __    
/ _ \___  __ _  (_)__  ___ ____  / /_   
/ // / _ \/  ' \/ / _ \/ _ `/ _ \/ __/   
/____/\___/_/_/_/_/_//_/\_,_/_//_/\__/    
/ __(_)__ ____ ___ _  _____ _/ /_ _____ 
/ _// / _ `/ -_) _ \ |/ / _ `/ / // / -_)
/___/_/\_, /\__/_//_/___/\_,_/_/\_,_/\__/ 
    /___/                               
""")
    
    matrix = input_squareMatrix()
    matrix = np.array(matrix, dtype=float)

    eig, x = power_method(matrix, iter=2000, tolerance=1e-9)

    if eig is None:
        print("Power method did not converge to a unique dominant eigenvalue.")
    else:
        print(f"Dominant eigenvalue: {eig}")
        print(f"Dominant eigenvector: {x}")
    print("Press Enter to go back to main menu...")
    input()
    mainMenu()

def svd():
    clear()
    print(r"""                      
 ,---.,--.   ,--.,------.   
'   .-'\  `.'  / |  .-.  \  
`.  `-. \     /  |  |  \  : 
.-'    | \   /   |  '--'  / 
`-----'   `-'    `-------'                         
""")
    np.set_printoptions(precision=4, suppress=True)
    A = np.array(input_matrix()) #A = U Σ VT
    m, n = A.shape
    r = min(m, n)

    ATA = A.T @ A
    lamV, V = np.linalg.eigh(ATA)
    idxV = lamV.argsort()[::-1]
    lamV = lamV[idxV]
    V = V[:, idxV]

    #lamU = np.clip(lamU, 0.0, None)
    lamV = np.clip(lamV, 0.0, None)
    sigma = np.sqrt(lamV) #averaging in case of mismatch due to floating point rounding errors

    eps = np.finfo(float).eps
    tol = max(m, n) * eps * (sigma[0] if r else 0.0)
    k = int(np.sum(sigma > tol)) # numerical rank
    k = min(k, r)

    U = np.zeros((m, m))
    U[:, :k] = (A @ V[:, :k]) / sigma[:k].reshape(1, -1)

    d = np.sign(np.diag(U[:, :k].T @ A @ V[:, :k]))
    d[d == 0] = 1.0
    U[:, :k] *= d.reshape(1, -1)
    V[:, :k] *= d.reshape(1, -1)

    if m > k:
        Z = np.random.randn(m, m - k)
        Z -= U[:, :k] @ (U[:, :k].T @ Z)
        U2, _ = np.linalg.qr(Z)
        U[:, k:] = U2

    Sigma = np.zeros((m, n))
    Sigma[np.arange(r), np.arange(r)] = sigma[:r]

    def zapsmall(M, Aref=None, rel=50*np.finfo(float).eps, abs_=0.0):
        scale = np.linalg.norm(A if Aref is None else Aref, ord=np.inf)
        thr = abs_ + rel * scale
        M[np.abs(M) < thr] = 0.0
        return M

    U = zapsmall(U, A)
    V = zapsmall(V, A)
    Sigma = zapsmall(Sigma, A)

    print(f"\n\nU = {U};\n\nΣ = {Sigma};\n\nV_T = {V.T}")
    print(f"Check\nA = U Σ V_T = {zapsmall(U @ Sigma @ V.T, A)};")
    print("Press Enter to go back to main menu...")
    input()
    mainMenu()
    
if __name__ == "__main__":
    mainMenu()
