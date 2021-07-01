#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()


f = cgi.FieldStorage()
cmd = f.getvalue("x")

o = subprocess.getoutput("kubectl " + cmd + " --kubeconfig admin.conf")

print("<body>")
print('<h1 style="color:#000002;" >Output</h1>')
print("<pre>{}</pre>".format(o))
print("</body>")



#print("Devanshu Singh")
