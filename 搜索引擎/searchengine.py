import pandas as pd
from io import StringIO

# 逐行读取CSV文件，跳过格式错误的行
pagerank_data = []
index_data = []

# 更新文件路径
pagerank_path = r'D:\搜索引擎\pagerank计算\pagerank_values_clean.csv'
index_path = r'D:\搜索引擎\倒排索引\inverted_index.csv'

with open(pagerank_path, 'r', encoding='utf-8') as file:
    for line in file:
        try:
            row = pd.read_csv(StringIO(line), header=None).values.flatten()
            pagerank_data.append(row)
        except pd.errors.ParserError:
            print(f"Ignoring malformed line: {line}")

with open(index_path, 'r', encoding='utf-8') as file:
    for line in file:
        try:
            row = pd.read_csv(StringIO(line), header=None).values.flatten()
            index_data.append(row)
        except pd.errors.ParserError:
            print(f"Ignoring malformed line: {line}")

# 构建数据结构
pagerank_df = pd.DataFrame(pagerank_data)
index_df = pd.DataFrame(index_data)

pagerank_dict = dict(zip(pagerank_df[0], pagerank_df[1]))

index_dict = {}
for row in index_df.itertuples(index=False):
    word = row[0]
    files = row[1:]  # 从第二列开始取文件列表
    index_dict[word] = files

# 用户输入关键字
user_input = input("请输入关键字: ")

# 检索相关文件列表
if user_input in index_dict:
    matching_files = index_dict[user_input]
    # 获取对应PageRank值，排除"未找到对应Pagerank值"的情况
    result = [(file, pagerank_dict.get(file, float('-inf'))) for file in matching_files]
    # 按PageRank值排序，排除"未找到对应Pagerank值"的情况
    sorted_result = sorted(result, key=lambda x: x[1], reverse=True)
    # 输出结果
    print("搜索结果:")
    for file, pagerank in sorted_result:
        if pagerank != float('-inf'):
            print(f"文件: {file}, PageRank值: {pagerank}")
        elif file is not None:
            print(f"文件: {file}, 未找到对应Pagerank值")
else:
    print("未找到匹配的文件。")
