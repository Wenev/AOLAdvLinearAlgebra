import numpy as np
import os

# Clear Screen
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# For Matrix Input
def input_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter the matrix values row by row (separated by spaces):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)

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

    # Your diagonalizable matrix logic here

def LUDecomposition():
    clear()
    print(r"""
__   __  __  ___                                   _ __  _         
/ /  / / / / / _ \___ _______  __ _  ___  ___  ___ (_) /_(_)__  ___ 
/ /__/ /_/ / / // / -_) __/ _ \/  ' \/ _ \/ _ \(_-</ / __/ / _ \/ _ \
/____/\____/ /____/\__/\__/\___/_/_/_/ .__/\___/___/_/\__/_/\___/_//_/
                                    /_/                                
""")


    matrix = input_matrix()
    # Your LU Decomposition matrix logic here

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

    # Your dominant eigenvalue logic here

def svd():
    clear()
    print(r"""                      
 ,---.,--.   ,--.,------.   
'   .-'\  `.'  / |  .-.  \  
`.  `-. \     /  |  |  \  : 
.-'    | \   /   |  '--'  / 
`-----'   `-'    `-------'                         
""")

def main_menu():
    
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

# Run the menu
if __name__ == "__main__":
    main_menu()
