import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

df = pd.read_csv(r'Data\all_data.csv')

# Handle NaN values in the 'Product' column
df = df.dropna(subset=['Product'])

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['Product'])

# Optimal number of clusters using the Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Elbow graph
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Choose the number of clusters based on the Elbow Method (e.g., 6)
n_clusters = 6
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
y_kmeans = kmeans.fit_predict(X)

# Add the cluster labels to the DataFrame
df['Category'] = y_kmeans

# Reduce dimensions to 3D for visualization
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X.toarray())

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=y_kmeans, cmap='rainbow')

# Add labels and title
ax.set_title('3D Product Clustering')
ax.set_xlabel('PCA 1')
ax.set_ylabel('PCA 2')
ax.set_zlabel('PCA 3')

# Show plot
plt.show()

# Save the clustered data to a new CSV file
df[['Product', 'Purchase Address', 'Category']].to_csv('clustered_product_data.csv', index=False)

print("Clustering completed")
