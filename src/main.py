import frontmatter
import os
import networkx as nx
import warnings
import networkx.drawing.nx_pydot

warnings.filterwarnings("ignore", category=DeprecationWarning)

G = nx.DiGraph()

G.graph['graph'] = {'rankdir': 'LR'}
G.graph['node'] = {'shape': 'circle', 'color': 'red'}
G.graph['edges'] = {'arrowsize': '4.0', 'dir': 'forward', 'arrowhead': 'empty'}

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
            G.add_edges_from(edges, arrowhead='empty')

graph = networkx.drawing.nx_pydot.to_pydot(G)

graph.set_bgcolor("transparent")

graph.write_raw("output_raw.dot")
graph.write_png("output.png")
