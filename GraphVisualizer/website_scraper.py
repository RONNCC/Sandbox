"""
Scrapes MAL for animedata given a URL starting link!

No parallelization because currently Google App Engine doesn't have much in the way of free computing power :/
"""

import re,urllib,networkx as nx, pylab as plt
from collections import deque
url="http://myanimelist.net/anime/3389/Bus_Gamer/userrecs"
pattern = re.compile('(?<=<div style="margin-bottom: 2px;"><a href=").*?(?=")')
G = nx.Graph()
q = deque([[(x[29:]).split('/') for x in [url]][0][0:2]])
for x in range(10):
    ci,cn = q.popleft()
    urld = urllib.urlopen("http://myanimelist.net/anime/"+ci+"/"+cn+"/userrecs").read()
    d = [(x[29:]).split('/') for x in pattern.findall(urld)]
    for z in d:
        q.append((z[0],z[1]))
        G.add_edge(cn,unicode(z[1],'utf-8'))

nx.draw(G)
plt.show()
#nx.write_gexf(G,"MALgraph.gexf")
