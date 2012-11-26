##Calc file sizes for each format starting from top folder. Is recursive.
import os
sizes = {}
toppath = 'H:\\Ronnie\\Storage\\Books'
totalsize = 0
def updatedict(arg,dirname,names):
    global totalsize
    try:
        for x in names:
            path = dirname+'\\'+x
            ext = os.path.splitext(path)[1]
            size = os.stat(path).st_size*1.0/1000000
            if ext in sizes:
                sizes[ext]+=size
            else:
                sizes[ext]=size
            totalsize+=size
    except WindowsError,e:
        pass
os.path.walk(toppath,updatedict,1)
print 'TOTALSIZE:',totalsize,'\n'
print sorted(sizes)
