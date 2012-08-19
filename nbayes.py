"""
 Columns with Incomplete Data Are Ignored
 The case of the text (Upper/Lower/Mixed) is important as those are unique header identifiers
"""
from numpy import genfromtxt,asarray, rollaxis,where,roll,delete,nonzero
#define which column is to be determined using all the others as observation columns
#columns all need to have unique names
result_column = "Stolen"

class nbayes():
    def readInData(self,filename):
        # traditionally would use numpy's genfromtext() here, but the comment argument of it
        # seems broken. As such an issue was opened on numpy's github.
        # still being used, but this is specific for the files used here (the lines to skip)
        columns = None
        with open(filename) as fn:
    ##        while not columns:
    ##            c = fn.readline()
    ##            if c.find("#$") != -1:
    ##                columns = c.replace("#$","").split()
    ##        assert columns!= None, "Columns Not Labeled"
    ##        columns = asarray(columns)
            try:
                a = genfromtxt(fn,dtype=None,comments='#',skip_header=2,names=True)
            except ValueError:
                print "Error: Number of column headers does not match the number of complete data columns"
                exit(1)
        columns = asarray(a.dtype.names)
        self.columns=columns
        it = delete(columns,nonzero(columns==result_column))
        self.it = it
    def classify(self):
        print self.it


        
        #transpose the axis such that the result axis is always last
        #columns = asarray(columns)
        #assert a.shape[1] == len(columns), "The number of column headers does not equal the amount of complete data columns"

        #print a[a["Type"] == "Sports"]
        #print len(a[a["Type"] == "Sports"])
        #print a.dtype
    ##    print 'COL',columns
    ##    print 'A',a
    ##    print ''
        #a = roll(a,len(columns) - where(columns==result_column)[0] -1 , 1)

def main():
    nb = nbayes()
    nb.readInData('data\cars.txt')
    nb.classify()
if __name__=='__main__':
    main()
