# Create a login window  - this should have UserName and Password labels and Entry textboxes, and a "Login" button.  

import easygui as eg
msg = "Please log in."
title = "Bottom secret"
fields = ["UserName", "Password"]

authentication = eg.multpasswordbox(msg, title, fields)

while 1:
    if authentication is None: break
    errmsg = "Error"
    for i in range(len(fields)):
        print(i, errmsg)
        if authentication[i].strip() == "":
            errmsg = errmsg + ('"%s" is a required field.\n\n' % fields[i])
    if errmsg == "Error":
        break  # no problems found
    authentication = eg.multpasswordbox(errmsg, title, fields, authentication)

print(authentication)