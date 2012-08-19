from numpy import genfromtxt,asarray, rollaxis,where,roll
#define which column is to be determined using all the others as observation columns
#columns all need to have unique names
result_column = "Stolen"

class nbayes():
    def __init__(dataset):
        self.data = dataset
def readInData(filename):
    # traditionally would use numpy's genfromtext() here, but the comment argument of it
    # seems broken. As such an issue was opened on numpy's github.
    # still being used, but this is specific for the files used here (the lines to skip)
    columns = None
    with open(filename) as fn:
        while not columns:
            c = fn.readline()
            if c.find("#$") != -1:
                columns = c.replace("#$","").split()
        assert columns!= None, "Columns Not Labeled"
        columns = asarray(columns)
        a = genfromtxt(fn,dtype=None,comments='#',skip_header=2)
    #transpose the axis such that the result axis is always last
    columns = asarray(columns)
##    print 'COL',columns
##    print 'A',a
##    print ''
    a = roll(a,len(columns) - where(columns==result_column)[0] -1 , 1)
    
readInData('data\cars.txt')
