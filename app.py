from flask import Flask
app = Flask(__name__)
import subprocess
@app.route("/<size>")
def hello_world(size):
    if int(size)>0 and int(size)<30:
        cmd = "python index.py " + str(size)
        proc=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
        output=proc.communicate()[0]
    else:
        return "invalid integer"
    return "<pre>" +  str(output,'utf-8') +"</pre>"