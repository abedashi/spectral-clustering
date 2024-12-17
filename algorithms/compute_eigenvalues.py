import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse.linalg as spla

def compute_eigen(L, k):
    # Compute eigenvalues using Arnoldi method 
    vals, vecs = spla.eigsh(L, k=k, which='SM', v0=None, maxiter=1000, tol=1e-6)

    # Sort the eigenvalues in ascending order and plot them
    sorted_indices = np.argsort(vals)
    sorted_vals = vals[sorted_indices]

    return vals, vecs, sorted_vals

def num_cluster(vals, k, title):
    # Plot the eigenvalues to visualize gaps
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, k+1), vals, 'o-', label='Eigenvalues')
    plt.xlabel('Eigenvalue index')
    plt.ylabel('Eigenvalue')
    plt.title(f"{title} - Eigenvalue Gap Analysis")
    plt.grid(True)

    # Compute the gaps between consecutive eigenvalues
    gaps = np.diff(vals)

    # Identify the largest gap to determine the number of clusters
    num_clusters = np.argmax(gaps) + 1  # Add 1 because indexing starts at 0

    # Highlight the largest gap on the plot
    plt.plot(num_clusters, vals[num_clusters - 1], 'ro', label='Largest Gap')
    plt.legend()
    plt.show()

    print(f'Number of clusters for {title} based on largest eigenvalue gap: {num_clusters}')
    return num_clusters