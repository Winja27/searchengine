import networkx as nx
import pandas as pd

file_path = 'D:\搜索引擎\网页链接图\graph.gexf'
G = nx.read_gexf(file_path)

pagerank_values = nx.pagerank(G)

df = pd.DataFrame(list(pagerank_values.items()), columns=['Node', 'PageRank'])

print(df)

csv_file_path = 'pagerank_values.csv'
df.to_csv(csv_file_path, index=False)
