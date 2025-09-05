import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('.github/data/commit.csv', parse_dates=['Date'])

df['Date'] = df['Date'].dt.date

plt.figure(figsize=(10, 6))
df['Date'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Date')
plt.ylabel('Number of Commits')
plt.title('Commits count by Date')
plt.tight_layout()
plt.savefig('.github/data/commit_graph.png')
