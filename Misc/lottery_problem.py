from sys import argv
a = [100,10,2,1]
#def prob(x):
#        a = (x[3]+1)/x[2] + (1 if (x[3]+1)%x[2] != 0 else 0)
#        return sum([(x[1]-n)/(1.0*(x[0]-n)) for n in xrange(0,a)])
def conp(x):
        return sum([(x[1]-n)/(1.0*(x[0]-n)) for n in
                    xrange(0,(x[3]+1)/x[2] +
                    (1 if (x[3]+1)%x[2] != 0 else 0))])
def test():
        for x in [ [100,10,2,1],[100,10,2,2],[10,10,5,1],]:
                print x,prob(x)
print conp([int(x) for x in argv[1:]])
