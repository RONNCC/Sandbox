"""
A* Search Written by Shomiron Ghose (2012)

**No copying**

-> goal was brevity, not readability... even though that's unpythonic.
"""



import sys,math,itertools
try:
	adj,dist = {},{}
	xy = dict([ (i,(int(j),int(k)))  for i,j,k in [z.split(',') for z in [y.replace('\n','') for y in open('xy.txt').readlines()]]])
	[[dist.update([((x,y),d),((y,x),d)])for z in ([[0],adj.update([[(x,list(itertools.chain(adj[x],[y]))),(y,list(itertools.chain(adj[y],[x])) )] for z in [[0],adj.update([(z,[]) for z in [x,y] if z not in adj])][0]][0])][0]) for d in [list(itertools.starmap(lambda x,y:math.sqrt(sum(itertools.imap(lambda x1,x2: (x1-x2)**2, xy[x],xy[y]))),[(x,y)]))[0]]] for x,y in [z.split(',') for z in [y.replace('\n','') for y in open('edges.txt').readlines()]]]
	def func(city1, city2):
		q = [[0,list(itertools.starmap(lambda x,y:math.sqrt(sum(itertools.imap(lambda x1,x2: (x1-x2)**2, xy[x],xy[y]))),[(city1,city2)]))[0],city1]]
		while(True):
			popped = q.pop(0)
			if popped[-1]==city2: print "found", "dist:",popped[0];break
			[[q.append([popped[0]+list(itertools.starmap(lambda x,y:math.sqrt(sum(itertools.imap(lambda x1,x2: (x1-x2)**2, xy[x],xy[y]))),[(path[-1],n)]))[0],list(itertools.starmap(lambda x,y:math.sqrt(sum(itertools.imap(lambda x1,x2: (x1-x2)**2, xy[x],xy[y]))),[(n,city2)]))[0]] + list(itertools.chain(popped[2:],[n]))) for n in adj[popped[2:][-1]]] for path in [popped[2:]]]
			q = sorted(q,key=lambda l:l[0]+l[1])
	func(sys.argv[1],sys.argv[2])
except KeyError:
	print "Sorry that city doesn't exist"

	

"""
import sys,math,itertools
try:
	adj,dist = {},{}
	xy = dict([ (i,(int(j),int(k)))  for i,j,k in [z.split(',') for z in [y.replace('\n','') for y in open('xy.txt').readlines()]]])
	calcDist= lambda x,y:math.sqrt(sum(itertools.imap(lambda x1,x2: (x1-x2)**2, xy[x],xy[y])))
	[[dist.update([((x,y),d),((y,x),d)])for z in ([[0],adj.update([[(x,list(itertools.chain(adj[x],[y]))),(y,list(itertools.chain(adj[y],[x])) )] for z in 
	[[0],adj.update([(z,[]) for z in [x,y] if z not in adj])][0]][0])][0]) for d in 
	[calcDist(x,y)]] for x,y in [z.split(',') for z in [y.replace('\n','') for y in open('edges.txt').readlines()]]]
	#[calcDist(x,y)]] for x,y in [z.split(',') for z in [y.replace('\n','') for y in open('edges.txt').readlines()]]]
	def func(city1, city2):
		q = [[0,calcDist(city1,city2),city1]]
		while(True):
			popped = q.pop(0)
			if popped[-1]==city2: print "found", "dist:",popped[0];break
			[[q.append([popped[0]+calcDist(path[-1],n),calcDist(n,city2)] + list(itertools.chain(popped[2:],[n]))) for n in adj[popped[2:][-1]]] for path in [popped[2:]]]
			q = sorted(q,key=lambda l:l[0]+l[1])
	func(sys.argv[1],sys.argv[2])
except KeyError:
	print "Sorry that city doesn't exist"

"""