import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

df = pd.read_csv(r'Data\all_data.csv')

# Handle NaN in 'Product'
#df['Product'].fillna('', inplace=True)  
df = df.dropna(subset=['Product']) 

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['Product'])

#Optimal number of clusters using the Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

#Elbow graph
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Choose the number of clusters based on the Elbow Method (e.g., 4)
n_clusters = 6
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
y_kmeans = kmeans.fit_predict(X)

# Add the cluster labels to the DataFrame
df['Category'] = y_kmeans

# Optionally reduce dimensions for visualization (2D Plot)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X.toarray())
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_kmeans, cmap='rainbow')
plt.title('Product Clustering')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.show()


#df.to_csv('clustered_product_data.csv', index=False)
df[['Product', 'Purchase Address', 'Category']].to_csv('clustered_product_data.csv', index=False)

print("Clustering completed")
