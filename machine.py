import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('D:/Documents/Downloads/imdb_top_1000.csv')


columns_to_drop = ['Poster_Link', 'Overview', 'Meta_score', 'Star1', 'Star2', 'Star3', 'Star4', 'No_of_Votes', 'Gross']
df = df.drop(columns=columns_to_drop)


df = df.dropna()


genre_counts = df['Genre'].value_counts()


genre_df = pd.DataFrame(genre_counts).reset_index()
genre_df.columns = ['Genre', 'Count']


plt.figure(figsize=(12, 6))
plt.bar(genre_df['Genre'], genre_df['Count'])
plt.xlabel('Genre')
plt.ylabel('Count')
plt.title('Most Popular Genre of Movies and TV Shows')
plt.xticks(rotation=90)
plt.show()


director_counts = df['Director'].value_counts()

director_df = pd.DataFrame(director_counts).reset_index()
director_df.columns = ['Director', 'Count']


plt.figure(figsize=(12, 6))
plt.bar(director_df['Director'], director_df['Count'])
plt.xlabel('Director')
plt.ylabel('Count')
plt.title('Director with the Most Top-Rated Movies and TV Shows')
plt.xticks(rotation=90)
plt.show()
