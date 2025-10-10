import numpy as np

def isDiagonalizable():
    print("\n🔹 Checking if matrix is diagonalizable...\n")
    # Your diagonalizable matrix logic here

def LUDecomposition():
    print("\n🔹 Performing LU Decomposition...\n")
    # Your LU decomposition logic here

def dominantEigenvalue():
    print("\n🔹 Finding dominant eigenvalue...\n")
    # Your dominant eigenvalue logic here

def svd():
    print("\n🔹 Performing Singular Value Decomposition (SVD)...\n")
    # Your SVD logic here

def main_menu():
    while True:
        print("\n=== MATRIX ANALYZER ===")
        print("1. Check if Matrix is Diagonalizable")
        print("2. Perform LU Decomposition")
        print("3. Find Dominant Eigenvalue")
        print("4. Singular Value Decomposition (SVD)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            isDiagonalizable()
        elif choice == "2":
            LUDecomposition()
        elif choice == "3":
            dominantEigenvalue()
        elif choice == "4":
            svd()
        elif choice == "5":
            print("\n👋 Exiting Matrix Analyzer Tool. Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number from 1 to 5.")

# Run the menu
if __name__ == "__main__":
    main_menu()
