import frontmatter
from pyvis.network import Network
import os
import networkx as nx


G = nx.DiGraph()

path = "../md_testfiles/"
dir_list = os.listdir(path)

for file in dir_list:
    with open(path + file) as f:
        metadata, content = frontmatter.parse(f.read())
        G.add_node(metadata['title'])

        edges = []
        destinations = metadata['connected']
        if destinations is not None:
            for destination in destinations:
                edges.append((metadata['title'], destination))
            G.add_edges_from(edges)

print(G.edges)

net = Network(directed=True)
net.from_nx(G)

net.toggle_physics(False)
net.show_buttons(filter_=['physics'])
net.show('graph.html', notebook=False)
