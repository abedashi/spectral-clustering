import numpy as np

from scipy.sparse.linalg import eigsh

def compute_connected_components(L, tol=1e-5):
    # Compute the smallest eigenvalues
    eigenvalues, _ = eigsh(L, k=10, which='SM')  # Compute 10 smallest eigenvalues
    # Count eigenvalues close to zero (within tolerance)
    num_connected_components = np.sum(eigenvalues < tol)
    return num_connected_components
