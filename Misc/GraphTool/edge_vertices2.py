
import graph_tool as gt
import graph_tool.topology as gtt

G = gt.Graph(directed=False)
G.add_vertex(4)

for s,t in [(0,1), (2,3), (0,2)]:
    G.add_edge(G.vertex(s), G.vertex(t))

match, is_maximal = gtt.max_cardinality_matching(G)

GV = gt.GraphView(G, efilt=match)

for edge in GV.edges():
    print GV.vertex_index[edge.source()]

