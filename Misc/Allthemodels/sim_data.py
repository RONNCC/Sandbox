import sklearn.linear_model as lm
import sklearn.semi_supervised as ss
import sklearn.tree as tr
from sklearn import svm
import sklearn.naive_bayes as nb
import sklearn.ensemble as ens
import numpy as np
from multiprocessing import Pool

FN="AA_data.csv"
COLUMNS=(4,)
r = np.loadtxt(open(FN,"rb"),delimiter=",",skiprows=1,usecols=COLUMNS)[::-1]
xn = r.shape[0]
X=[[x] for x in range(xn-1)]
Y=r[:-1]
CLASSIFIERS={
"SGD":lm.SGDClassifier(),
#"ARDRegression":lm.ARDRegression(compute_score=True),
"LinReg":lm.LinearRegression(),
"BayesianRidge":lm.BayesianRidge(compute_score=True),
"LASSO:0.1":lm.Lasso(alpha=0.1),
"LASSO:0.01":lm.Lasso(alpha=0.01),
#"PassiveAggressiveRegressor:10":lm.PassiveAggressiveRegressor(n_iter=10),
#"PassiveAggressiveRegressor:20":lm.PassiveAggressiveRegressor(n_iter=20),
"LassoLars":lm.LassoLars(alpha=.1),
"LassoCV":lm.LassoCV(),
"LogReg":lm.LogisticRegression(),

"NaiveBayes":nb.GaussianNB(),

"LabelSpreading:rbf":ss.LabelSpreading(kernel='rbf'),
"LabelSpreading:knn":ss.LabelSpreading(kernel='knn'),



"SVM:rbf":svm.SVC(kernel='rbf'),
"SVM:sigmoid:2":svm.SVC(kernel='sigmoid',degree=2),
"SVM:sigmoid:3":svm.SVC(kernel='sigmoid',degree=3),
"SVM:sigmoid:4":svm.SVC(kernel='sigmoid',degree=4),
#"SVM:sigmoid:5":svm.SVC(kernel='sigmoid',degree=5),
#"SVM:sigmoid:6":svm.SVC(kernel='sigmoid',degree=6),
#"SVM:sigmoid:7":svm.SVC(kernel='sigmoid',degree=7),
#"SVM:sigmoid:8":svm.SVC(kernel='sigmoid',degree=8),
#"SVM:sigmoid:9":svm.SVC(kernel='sigmoid',degree=9),
#"SVM:sigmoid:10":svm.SVC(kernel='sigmoid',degree=10),
#"SVM:poly:1":svm.SVC(kernel='poly',degree=1),
#"SVM:poly:2":svm.SVC(kernel='poly',degree=2),
#"SVM:poly:3":svm.SVC(kernel='poly',degree=3),
#"SVM:poly:4":svm.SVC(kernel='poly',degree=4),
#"SVM:poly:5":svm.SVC(kernel='poly',degree=5),
#"SVM:poly:6":svm.SVC(kernel='poly',degree=6),
#"SVM:poly:7":svm.SVC(kernel='poly',degree=7),
#"SVM:poly:8":svm.SVC(kernel='poly',degree=8),
#"SVM:poly:9":svm.SVC(kernel='poly',degree=9),
"SVM:poly:10":svm.SVC(kernel='poly',degree=10),

"DecisionTreeRegressor":tr.DecisionTreeRegressor(),
"DecisionTreeClassifier":tr.DecisionTreeClassifier(),
"RandomForestClassifier:10":ens.RandomForestClassifier(n_estimators=10),
#"RandomForestClassifier:20":ens.RandomForestClassifier(n_estimators=20),
#"RandomForestClassifier:30":ens.RandomForestClassifier(n_estimators=30),
"ExtraForestClassifier:10":ens.ExtraTreesClassifier(n_estimators=10),
#"ExtraForestClassifier:20":ens.ExtraTreesClassifier(n_estimators=20),
#"ExtraForestClassifier:30":ens.ExtraTreesClassifier(n_estimators=30),

    }
actual=r[-1]

def runTest(k):
	e=CLASSIFIERS[k]
	p = e.predict([xn])
	print k,'difference: ','\t',abs(actual-p),'\t','percent diff: ',(abs((p-actual))/(1.0*actual)*100.)

def attempted_parallel():
	P = Pool()
	P.map(runTest,CLASSIFIERS.keys(),1)

def serial():
	for k,e in CLASSIFIERS.items():
		print 'working on',k
		e.fit(X,Y)
	     	p  =e.predict([xn])
	     	print k,'difference: ','\t',abs(actual-p),'\t','percent diff: ',(abs((p-actual))/(1.0*actual)*100.)

serial()
