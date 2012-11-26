import os
from pyPdf import PdfFileWriter, PdfFileReader
os.chdir("C:\Users\Shomiron\Desktop\Intro to\Intro to v2")


output = PdfFileWriter()
flist = os.listdir(os.getcwd())
c = 0
a = open("MalformedPdfs.txt",'w')
for x in flist:
    c+=1
    split = os.path.splitext(x)
    if split[1] == '.pdf':
        with open(x,"rb") as f:
            try:
                input1 = PdfFileReader(f)
                title = input1.getDocumentInfo().title
            except ValueError:
                print 'Malformed pdf-value : {}'.format(split[0])
                a.write("Malformed pdf-value: " + split[0]+"\n")
            except AttributeError:
                print 'Malformed pdf-attribute : {}'.format(split[0])
                a.write("Malformed pdf-attribute: " + split[0]+"\n")
            except Exception:
                print 'Decrypt Error'
                a.write('Decrypt Error: '+ split[0]+"\n")
            else:
                if title != None and title != '':
                    # print the title of document1.pdf
                    try:
                        print "Read title: {} actual= {}".format(str(split[0]), str(title))
                    except UnicodeEncodeError:
                        print "it's in ascii"
                        a.write(split[0]+"\n")
                    # print how many pages input1 has:
                    print "%s has %s pages." % (x,input1.getNumPages())

print 'LOOKED AT {} FILES'.format(c)
a.close()
