from scipy.sparse import diags

def compute_degree_matrix(W):
    degrees = W.sum(axis=1).A.flatten()  # Sum of each row (as array)
    D = diags(degrees, format='csr')  # Create diagonal matrix in sparse format
    return D

def compute_laplacian_matrix(W):
    D = compute_degree_matrix(W)  # Degree matrix
    L = D - W  # Subtract sparse matrices
    return L
