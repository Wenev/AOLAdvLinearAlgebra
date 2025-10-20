import numpy as np

def power_method(A, iter=2000, tolerance=1e-9):
    n, _ = A.shape
    x = np.ones(n)

    x = x/np.linalg.norm(x)

    eigen_start = 0
    
    for i in range(iter):
        Ax = A @ x
        x_new = Ax / np.linalg.norm(Ax)
        eigen_new = np.dot(x_new.T, Ax) / np.dot(x_new.T, x_new)
        if abs(eigen_new - eigen_start) < tolerance:
            return eigen_new, x_new
        x = x_new
        eigen_start = eigen_new
    return eigen_start, x
