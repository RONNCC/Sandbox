##Delete empty folders Is recursive.
import os
sizes = {}
toppath = 'C:\\Program Files'
totalsize = 0
empty = []
visited =0
count = 0
def updatedict(arg,dirname,names):
    global visited,count
    global totalsize
    visited+=1
    try:
        if len(names) == 0: empty.append(dirname)
    except WindowsError,e:
        pass
    if count == 500:
        print visited
        count=0
    count+=1
os.path.walk(toppath,updatedict,1)
print len(empty)
print empty
