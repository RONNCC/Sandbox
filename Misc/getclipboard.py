import pycurl
from Tkinter import Tk
from StringIO import StringIO
devkey = '013d746383e9913cb49ca403a6982c0d'
r=Tk()
imageurl=r.selection_get(selection="CLIPBOARD")
#imageurl="http://www.barkpurrandinsure.com/wp-content/uploads/2011/05/cat2.bmp"
c=pycurl.Curl()
w =StringIO()
values = [ ("key", devkey),("image",imageurl)]
c.setopt(c.URL, "http://api.imgur.com/2/upload.xml")
c.setopt(c.HTTPPOST, values)
c.setopt(pycurl.WRITEFUNCTION,w.write)
c.perform()
c.close()
a = w.getvalue()
r.clipboard_clear()
r.clipboard_append(a[a.rfind("<original>")+10:a.find("</original>")])
r.destroy()
exit()
