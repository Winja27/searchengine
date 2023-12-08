import os
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt


def extract_links(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
        links = soup.find_all('a', href=True)
        return [link['href'] for link in links]


def build_link_mapping(directory):
    link_mapping = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                source_page = os.path.join(root, file)
                target_pages = []
                links = extract_links(source_page)
                for link in links:
                    target_page = os.path.normpath(os.path.join(os.path.dirname(source_page), link))
                    target_pages.append(target_page)
                link_mapping[source_page] = target_pages
    return link_mapping


def build_graph(link_mapping):
    G = nx.Graph()
    for source_page, target_pages in link_mapping.items():
        for target_page in target_pages:
            G.add_edge(source_page, target_page)
    return G


if __name__ == "__main__":
    directory_path = r"D:\搜索引擎\爬虫和网页\网页"

    link_mapping = build_link_mapping(directory_path)
    print("Link Mapping:")
    for source, targets in link_mapping.items():
        print(f"{source} links to {', '.join(targets)}")

    graph = build_graph(link_mapping)
