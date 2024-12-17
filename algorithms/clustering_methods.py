from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans, AgglomerativeClustering

def k_mean(U, M, random_state):
    # Perform k-means clustering on the rows of U.
    kmeans = KMeans(n_clusters=M, random_state=random_state, n_init=10)
    cluster_labels = kmeans.fit_predict(U)
    return cluster_labels

def gmm_and_agg(X, num_clusters, random_state):
    # GMM Clustering
    gmm = GaussianMixture(n_components=num_clusters, random_state=random_state)
    gmm_labels = gmm.fit_predict(X)
    gmm_clusters = [X[gmm_labels == i] for i in range(num_clusters)]
    
    # Agglomerative Clustering
    agg = AgglomerativeClustering(n_clusters=num_clusters, linkage='ward')
    agg_label = agg.fit_predict(X)
    agg_clusters = [X[agg_label == i] for i in range(num_clusters)]

    return gmm_clusters, gmm_labels, agg_clusters, agg_label
