import re

from tensorflow.keras.preprocessing.text import Tokenizer


def remove_html_tags(input_text):
    clean_text = re.sub('<.*?>', '', input_text)
    return clean_text


tokenizer = Tokenizer()
with open(
        'D:\搜索引擎\爬虫和网页\网页\中国\A DNA barcode reference library of Neuroptera (Insecta, Neuropterida) from Beijing - PubMed.html',
        'r', encoding='utf-8') as file:
    # 读取文件全文内容
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
tokenizer.fit_on_texts(texts)
word_index = tokenizer.word_index
print(word_index)
