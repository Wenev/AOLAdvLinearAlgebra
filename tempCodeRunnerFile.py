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