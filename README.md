# searchengine
使用Python实现简单的搜索引擎
本次项目简单实现了一个搜索引擎，基于pagerank来进行网页的排序。还有很多可以完善的地方，期待大家指正。

爬虫和网页部分主要是爬取网页，这里对PubMed网站进行了爬取并存储，可以在spider.py文件中修改key和local_url值（分别对应不同的爬取范围和存储位置）。

分词部分主要对网页内容进行解析。由于PubMed网站结果较为清晰，所以主要解析了标题，日期，作者，摘要等内容，并形成网页对应词汇表，包含该网页所使用的单词。对于英文文本，使用Keras的Tokenizer进行文本分词。

倒排索引部分主要对词汇表进行解析。此代码使用了 defaultdict 来创建一个默认为列表的字典，确保相同的单词的文件列表会被追加到同一行。

网页链接图部分从HTML文件中提取链接，并构建链接映射关系形成图文件。

pagerank部分对图文件进行pagerank计算。注意，计算结果包含大量无效链接（YouTube、Tweet等），需要经过数据清洗方可使用。

搜索引擎部分负责用户交互。
