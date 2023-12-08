from tensorflow.keras.preprocessing.text import Tokenizer

# 创建Tokenizer对象
tokenizer = Tokenizer()

# 拟合文本数据
texts = ["Keras is easy to use for text processing.", "It integrates well with deep learning models."]
tokenizer.fit_on_texts(texts)

# 文本转换为序列
sequences = tokenizer.texts_to_sequences(texts)

# 查看词汇表
word_index = tokenizer.word_index

print("文本序列：", sequences)
print("词汇表：", word_index)
