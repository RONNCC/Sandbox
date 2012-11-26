from random import random
from math import exp
def main():
    ins = [ [1,0,0],[1,0,1],[1,1,0],[1,1,1]  ]
    outs = [ 0,1,1,0 ]
    mu = .5
    dr = .1
    weights =[ [random(),random(),random()], [random(),random(),random()], [random(),random(),random()],[random(),random(),random()] ]
    def padd(m,p,v):
        copy = weights[:]
        copy[m][p] = copy[m][p] + v
        return copy
    def sig(z):
        return 1/(1+exp(-z))
    def dot(x,y):
        assert len(x)==len(y), str("LENGTHS OF ARRAYS GIVEN NOT THE SAME" + str(x) + str(y))
        return sum([ x[c]*y[c] for c in xrange(len(x))])
    E = sum([ (outs[d] - sig( sum([ sig(dot(weights[c],ins[d]))  for c in xrange(len(outs))] )))**2 for d in xrange(len(outs))] )
    print 'E',E
    gens = 0
    #print weights,E
    while gens<1000:
        for ma in xrange(len(weights)):
            for pl in xrange(len(weights[ma])):
                lE = sum([ (outs[d] - sig( sum([ sig(dot(weights[c],ins[d]))  for c in xrange(len(outs))] )))**2 for d in xrange(len(outs))] )
                weights[ma][pl]+= mu*dr if sum([ (outs[d] - sig( sum([ sig(dot(padd(ma,pl,dr)[c],ins[d]))  for c in xrange(len(outs))] )))**2 for d in xrange(len(outs))] )  < lE else -1*mu*dr
        E = sum([ (outs[d] - sig( sum([ sig(dot(weights[c],ins[d]))  for c in xrange(len(outs))] )))**2 for d in xrange(len(outs))] )
        gens+=1

    ##TEST WEIGHTS
    for v in ins:
        print round(sig(sum([   sig(weights[0][0]*v[0] + weights[0][1]*v[1] + weights[0][2]*v[2]) + sig(weights[1][0]*v[0] + weights[1][1]*v[1] + weights[1][2]*v[2]) +  sig(weights[2][0]*v[0] + weights[2][1]*v[1] + weights[2][2]*v[2])]) ))

if __name__=='__main__':
    main()
