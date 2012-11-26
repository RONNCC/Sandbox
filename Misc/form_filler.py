import re
from mechanize import Browser

br = Browser()
br.set_handle_robots(False)
br.open("https://docs.google.com/spreadsheet/viewform?formkey=dEoydXFma1k3SjZRbk9xdkw1azI1ZXc6MQ&theme=0AX42CRMsmRFbUy03NThiZTgyMi1iNWZiLTQ1ZTUtYmJkZi00ZDMzODQ4NzA5YWI&ifq")
#br.select_form(name="order")
# Browser passes through unknown attributes (including methods)
# to the selected HTMLForm (from ClientForm).
#br["cheeses"] = ["mozzarella", "caerphilly"]  # (the method here is __setitem__)
#response = br.submit()  # submit current form
x = list(br.forms())
print type(x)
print '----'
br.select_form(x[0])
#br.select_form(name=list(str(br.forms())[0]))
print br
