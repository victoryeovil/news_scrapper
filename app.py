import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Read the DataFrame
df_updated = pd.read_csv("news_v1.csv")

# Drop the 'authors' column
df_updated.drop(columns=["authors"], inplace=True)

# Fill missing values in 'keywords' with the most common value
df_updated['keywords'] = df_updated['keywords'].fillna(df_updated['keywords'].mode()[0])

# Fill missing values in 'category' with the most common value
df_updated['category'] = df_updated['category'].fillna(df_updated['category'].mode()[0])

# Use CountVectorizer to create features from 'section'
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df_updated['section'])

# Apply KMeans clustering with 5 clusters
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)

# Add cluster labels to the DataFrame
df_updated['cluster'] = kmeans.labels_

# Define dictionary to map cluster labels to cluster names
cluster_names = {
    0: "Business",
    1: "Politics",
    2: "Arts",
    3: "Sport",
    4: "Celebrities"
}

# Map cluster labels to cluster names
df_updated['cluster_name'] = df_updated['cluster'].map(cluster_names)

# Define Streamlit app
st.title("Story Clustering Platform")
st.markdown("This platform displays clusters and related stories.")

# Display the unique cluster names as options
selected_cluster = st.selectbox("Select a cluster", df_updated['cluster_name'].unique())

# Filter the data based on the selected cluster
cluster_data = df_updated[df_updated['cluster_name'] == selected_cluster]

# Display the URLs of related stories in the selected cluster
st.subheader("Related Stories:")
for url in cluster_data['url']:
    st.write(url)

# Show the clusters with descriptive names
st.subheader("Cluster Analysis:")
for cluster_name in df_updated['cluster_name'].unique():
    cluster_data = df_updated[df_updated['cluster_name'] == cluster_name]
    st.write(f"Cluster {cluster_name}:")
    st.write(f"- Number of articles: {len(cluster_data)}")
    st.write(f"- Top categories: {cluster_data['section'].value_counts().head(3)}")
    st.write(f"- Top keywords: {cluster_data['keywords'].str.split(',').explode().value_counts().head(3)}")

# Visualize each cluster
st.subheader("Cluster Visualization:")
for cluster_name in df_updated['cluster_name'].unique():
    cluster_data = df_updated[df_updated['cluster_name'] == cluster_name]
    plt.figure(figsize=(10, 7))
    plt.scatter(cluster_data['content_length'], cluster_data['content_tier'], c=cluster_data['cluster'], cmap='viridis')
    plt.title(f"Cluster {cluster_name}")
    plt.xlabel("Content Length")
    plt.ylabel("Content Tier")
    plt.tight_layout()
    st.pyplot(plt)

