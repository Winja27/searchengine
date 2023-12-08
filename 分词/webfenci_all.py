import os
import re
from tensorflow.keras.preprocessing.text import Tokenizer


def remove_html_tags(input_text):
    clean_text = re.sub('<.*?>', '', input_text)
    return clean_text


def tokenize_and_save(file_path, output_dir):
    with open(file_path, 'r', encoding='utf-8') as file:
        cdata = file.read()

    pat2_title = "<title>(.*?)</title>"
    pat3_content = '<div class="abstract-content selected".*?>(.*?)</div>'
    pat4_date = '<span class="cit">(.*?)</span>'
    pat5_writer = '<a class="full-name".*?>(.*?)</a>'
    title = re.compile(pat2_title, re.S).findall(cdata)
    content = re.compile(pat3_content, re.S).findall(cdata)
    date = re.compile(pat4_date, re.S).findall(cdata)
    writer = re.compile(pat5_writer, re.S).findall(cdata)
    texts = title + content + date + writer
    text = "".join(texts)
    text_without_newlines = text.replace('\n', '')
    text_without_tags = remove_html_tags(text_without_newlines)

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([text_without_tags])

    word_index = tokenizer.word_index

    file_name = os.path.splitext(os.path.basename(file_path))[0]
    output_file_path = os.path.join(output_dir, f"{file_name}_word_index.txt")

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for word, index in word_index.items():
            output_file.write(f"{word}\n")

    print(f"词索引文件 {file_name} 已保存至 {output_file_path}")


def process_html_files(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                tokenize_and_save(file_path, output_dir)


# 指定输入和输出目录
input_directory = r'D:\搜索引擎\爬虫和网页\网页'
output_directory = r'D:\搜索引擎\分词\网页词汇表'  # 指定你想要保存结果的目录

process_html_files(input_directory, output_directory)
