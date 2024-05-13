import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
#import matplotlib.pyplot as plt

combined_df = pd.read_csv("combined_data_filled.csv")


# Vectorize 'category'
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(combined_df['category'])

# KMeans clustering
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
combined_df['cluster'] = kmeans.labels_

# Cluster names
cluster_names = {0: "Business", 1: "Politics", 2: "Arts", 3: "Sport"}
combined_df['cluster_name'] = combined_df['cluster'].map(cluster_names)

# Streamlit App
st.title("News Clustering Platform by Victor Marisa R207764L")
st.markdown("This web displays clusters and related stories. Source code is found through clicking the two buttons. The spyders are found in github and the colab is used to clean the data and create a csv to work with for clustering using this streamlit app")

st.markdown(
    """
    <div style="display: flex; justify-content: space-around;">
        <a href="https://github.com/victoryeovil/news_scrapper/" target="_blank">
            <button style="background-color: #24292f; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                GitHub
            </button>
        </a>
        <a href="https://colab.research.google.com/drive/1THIg-cdgeisjlGyzUW2D6OTgTk3F8A6j?usp=sharing" target="_blank">
            <button style="background-color: #4285f4; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                Google Colab
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Cluster selection
selected_cluster = st.selectbox("Select a cluster", combined_df['cluster_name'].unique())
cluster_data = combined_df[combined_df['cluster_name'] == selected_cluster]

# Display related stories
st.subheader("Related Stories:")
for url in cluster_data['link']:
    st.write(url)

# Cluster analysis
st.subheader("Cluster Analysis:")
for cluster_name in combined_df['cluster_name'].unique():
    cluster_data = combined_df[combined_df['cluster_name'] == cluster_name]
    st.write(f"Cluster {cluster_name}:")
    st.write(f"- Number of articles: {len(cluster_data)}")

    # Handle missing columns gracefully
    if 'section' in combined_df.columns:
        st.write(f"- Top categories: {cluster_data['section'].value_counts().head(3)}")
    if 'title' in combined_df.columns:
        st.write(f"- Top keywords: {cluster_data['title'].str.split(',').explode().value_counts().head(3)}")


