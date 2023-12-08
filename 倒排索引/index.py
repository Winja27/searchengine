import os
import csv
from collections import defaultdict

def build_inverted_index(vocabulary_directory, output_csv):
    inverted_index = defaultdict(list)

    for root, dirs, files in os.walk(vocabulary_directory):
        for vocab_file in files:
            file_path = os.path.join(root, vocab_file)
            with open(file_path, 'r', encoding='utf-8') as file:
                words = [line.strip() for line in file]

                for word in words:
                    if file_path not in inverted_index[word]:
                        inverted_index[word].append(file_path)

    # 将倒排索引写入CSV文件
    with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Word', 'Files'])

        for word, files in inverted_index.items():
            # 去除文件名中的 _word_index.txt 部分和 D:\搜索引擎\分词\网页词汇表\ 部分
            files = [os.path.splitext(os.path.basename(f))[0] for f in files]
            files = [f.replace(os.path.join(vocabulary_directory, ''), '') for f in files]
            csv_writer.writerow([word] + files)

    print(f"倒排索引已保存至 {output_csv}")

# 假设你的词汇表文件存储在目录 D:\搜索引擎\分词\网页词汇表
vocabulary_directory = r'D:\搜索引擎\分词\网页词汇表'

# 指定输出CSV文件路径
output_csv = 'inverted_index.csv'

# 调用函数建立倒排索引并保存到CSV文件
build_inverted_index(vocabulary_directory, output_csv)
