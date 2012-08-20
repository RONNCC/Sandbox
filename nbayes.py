"""
 Columns with Incomplete Data Are Ignored, column names need to be one word as otherwise the delimiter thinks it is multiple headings.
 Ex. 'Foot size' needs to be 'Footsize'
 The case of the text (Upper/Lower/Mixed) is important as those are unique header identifiers

Datasets:
    Cars data set from Eric Meisner (http://www.inf.u-szeged.hu/~ormandi/ai2/06-naiveBayes-example.pdf)
    Gender data set from Wikipedia (http://en.wikipedia.org/wiki/Naive_Bayes_classifier)

"""
from numpy import genfromtxt,asarray,where,delete,nonzero, unique,empty,fromiter,multiply
#define which column is to be determined using all the others as observation columns
#columns all need to have unique names
class nbayes():
    def readInData(self,filename):
        # traditionally would use numpy's genfromtext() here, but the comment argument of it
        # seems broken. As such an issue was opened on numpy's github.
        # still being used, but this is specific for the files used here (the lines to skip)
        columns = None
        with open(filename) as fn:
            try:
                a = genfromtxt(fn,dtype=None,comments='#',skip_header=2,names=True)
            except ValueError:
                print "Error: Number of column headers does not match the number of complete data columns"
                exit(1)
        self.data = a
        columns = asarray(a.dtype.names)
        self.columns=columns
        it = delete(columns,nonzero(columns==self.result_column))
        self.it = it
    def classify(self,attributes):
        #the attributes of the object to be classified
        attrs = attributes
        #options that it can be classified to
        r_options = unique(asarray(self.data[:][self.result_column]))
        # no prior assumption is made so the probability is 1/(classify options)
        p = 1./len(r_options)
        v = self.data[self.data[self.result_column] == "No"]

        # Made into a function so that different distributions can be used
        def mestimate(option):
            """
            Use the M-estimate to estimate P(a_i|v_j); the probability of an attribute a_i given the classification v_j out of set of possible classifications V     
            M-estimate from http://www.inf.u-szeged.hu/~ormandi/ai2/06-naiveBayes-example.pdf
            """
            # all of the records which have the classifier as option
            total = self.data[self.data[self.result_column] == option]
            total_num = len(total)
            #arbitrary equivalent sample size
            m = 3
            #calculate the m-estimate. *1.0 to ensure a decimal always returned
            mest = lambda nc: 1.0*(nc+m*p)/(total_num + m)
            attr_estimates = fromiter(( mest(len(total[total[k]==v])) for k,v in attrs.items()),float ,count=len(attrs))
            return p*multiply.reduce(attr_estimates)
            #probability of each possible classification
        probs = [(mestimate(classification),classification) for classification in r_options]
        return max(probs)[1]

        
def main():
    """
    Put classifier code in here!
     Test cases to be run below
    
     To run the test cases, do: 
     Test = test()
     Test.carstest()
    """
    Test = test()
    Test.iristest()
class test():
    def carstest(self):
        nb = nbayes()
        results = "Stolen"
        nb.result_column = results
        nb.readInData('data\cars.txt')
        attributes = {"Color":"Red","Type":"SUV","Origin":"Domestic"}
        print "Should be No,",':'.join([results,nb.classify(attributes)])
    def gendertest(self):
        nb = nbayes()
        results = "Sex"  
        nb.result_column = results
        nb.readInData('data\gender.txt')
        attributes = {"Height":6,"Weight":130,"Footsize":8}
        print "Should be Female,",': '.join([results,nb.classify(attributes)])
    def iristest(self):
        nb = nbayes()
        results = "Species"  
        nb.result_column = results		
        nb.readInData('data\iris.txt')
	
        # Three random (convenience sample) points from the data set
        attributes = {"Sepallength":6.7,"Sepalwidth":3.3,"Petallength":5.7,"Petalwidth":2.5}
        print "Should be I.virginica",': '.join([results,nb.classify(attributes)])

        attributes = {"Sepallength":6.1,"Sepalwidth":2.8,"Petallength":4.0,"Petalwidth":1.3}
        print "Should be I.versicolor",': '.join([results,nb.classify(attributes)])

        attributes = {"Sepallength":4.9,"Sepalwidth":3.1,"Petallength":1.5,"Petalwidth":0.2}
        print "Should be l.setosa",': '.join([results,nb.classify(attributes)])



    
    
if __name__=='__main__':
    main()
