import matplotlib.pyplot as plt

def datasets_plot(X1, title1, X2, title2):
    # Plot the first dataset
    plt.figure(figsize=(6, 6))
    plt.scatter(X1[:, 0], X1[:, 1], c='blue', alpha=0.7, edgecolor='k', label='Dataset 1')
    plt.title(title1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Plot the second dataset
    plt.figure(figsize=(6, 6))
    plt.scatter(X2[:, 0], X2[:, 1], c='green', alpha=0.7, edgecolor='k', label='Dataset 2')
    plt.title(title2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

def clusters_plot(clusters, num_clusters, title='Clusters', figsize=(8, 6)):
    # Set up the figure
    plt.figure(figsize=figsize)

    # Define a color palette
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

    # Loop through each cluster and plot its points
    for i in range(num_clusters):
        plt.scatter(
            clusters[i][:, 0], clusters[i][:, 1], 
            c=colors[i % len(colors)], 
            label=f'Cluster {i+1}', 
            alpha=0.7, edgecolor='k'
        )

    # Add title, legend, and axis labels
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.axis('equal')  # Ensure equal scaling of axes
    plt.grid(True)  # Add grid for better readability
    plt.show()
