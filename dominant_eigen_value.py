import numpy as np

def power_method(A, iter=2000, tolerance=1e-9):
    n, _ = A.shape
    x = np.ones(n, dtype=float)
    x = x / np.linalg.norm(x)

    eigen_start = 0.0
    x_prevprev = None 

    for _ in range(iter):
        Ax = A @ x
        normAx = np.linalg.norm(Ax)
        if normAx == 0.0:
            return 0.0, x

        x_new = Ax / normAx
        eigen_new = float(np.dot(x_new, Ax) / np.dot(x_new, x_new))

        if x_prevprev is not None:
            if abs(np.dot(x_new, x_prevprev)) > 1.0 - 1e-8:
                return None, None  # signal: no unique dominant eigenvalue (tie/complex)

        if abs(eigen_new - eigen_start) < tolerance:
            return eigen_new, x_new

        x_prevprev = x
        x = x_new
        eigen_start = eigen_new
        
    return None, None  # non-convergent within iter