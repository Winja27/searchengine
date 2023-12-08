import os
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt


def extract_links(html_path):
    """
    从HTML文件中提取链接。

    参数：
    html_path (str): HTML文件的路径。

    返回：
    list: 包含链接的列表。
    """
    with open(html_path, 'r', encoding='utf-8') as file:
        # 使用Beautiful Soup解析HTML内容
        soup = BeautifulSoup(file, 'lxml')
        # 查找所有包含href属性的a标签
        links = soup.find_all('a', href=True)
        # 提取链接的href属性值
        return [link['href'] for link in links]


def build_link_mapping(directory):
    """
    构建链接关系映射。

    参数：
    directory (str): 包含HTML文件的目录路径。

    返回：
    dict: 键是源网页，值是一个包含目标网页的列表。
    """
    link_mapping = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                # 构建源网页的完整路径
                source_page = os.path.join(root, file)
                target_pages = []
                # 提取源网页中的链接
                links = extract_links(source_page)
                for link in links:
                    # 构建目标网页的完整路径
                    target_page = os.path.normpath(os.path.join(os.path.dirname(source_page), link))
                    target_pages.append(target_page)
                # 将源网页及其链接关系添加到映射中
                link_mapping[source_page] = target_pages
    return link_mapping


def build_graph(link_mapping):
    """
    构建图形结构。

    参数：
    link_mapping (dict): 包含链接关系映射的字典。

    返回：
    nx.Graph: 表示链接关系的图形结构。
    """
    G = nx.Graph()
    for source_page, target_pages in link_mapping.items():
        for target_page in target_pages:
            # 添加边，表示链接关系
            G.add_edge(source_page, target_page)
    return G


def visualize_graph(G):
    """
    可视化图形结构。

    参数：
    G (nx.Graph): 表示链接关系的图形结构。
    """
    # 使用NetworkX和Matplotlib进行简单的图形可视化
    nx.draw(G, with_labels=True, font_size=8, node_size=1000, font_color='black')
    plt.show()


if __name__ == "__main__":
    directory_path = r"D:\搜索引擎\爬虫和网页\网页目录"

    # 构建链接关系映射
    link_mapping = build_link_mapping(directory_path)
    print("Link Mapping:")
    for source, targets in link_mapping.items():
        print(f"{source} links to {', '.join(targets)}")

    # 构建图形结构
    graph = build_graph(link_mapping)

    # 可视化图形结构
    visualize_graph(graph)
