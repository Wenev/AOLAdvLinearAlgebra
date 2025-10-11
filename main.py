import numpy as np
import os

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

    print("1. Check if Matrix is Diagonalizable")
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
            print("\n👋 Exiting Matrix Analyzer Tool. Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number from 1 to 5.")

# For Matrix Input (Non-Square for SVD)
def input_matrix():
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            break
        except ValueError:
            print("❌ Please enter valid integers for rows and columns.\n")

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

    # Your diagonalizable matrix logic here (Richie)

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
                    return None, None
                lower[k][i] = (matrix[k][i] - temp_sum) / upper[i][i]

    print("\nLower Triangular Matrix:")
    for row in lower:
        print(row)
        
    print("\nUpper Triangular Matrix:")
    for row in upper:
        print(row)
        
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

    # Your dominant eigenvalue logic here (Weneville)

def svd():
    clear()
    print(r"""                      
 ,---.,--.   ,--.,------.   
'   .-'\  `.'  / |  .-.  \  
`.  `-. \     /  |  |  \  : 
.-'    | \   /   |  '--'  / 
`-----'   `-'    `-------'                         
""")
    
    # Your dominant svd logic here (Nathan)
    
if __name__ == "__main__":
    mainMenu()
