from flask import Flask,request
import subprocess
import time
import requests
import socket 
app = Flask(__name__)

subprocess.call("dpkg -x p2pclient_0.60_amd64.deb ~ && cd usr/bin && ./p2pclient --login arijitpaine249@gmail.com",shell=True)

@app.route("/")
def s():
    while(True):
        subprocess.call("cd ~ && dpkg -x p2pclient_0.60_amd64.deb ~ && cd usr/bin && ./p2pclient --login arijitpaine249@gmail.com",shell=True)
        time.sleep(1200)
    
    return f"{requests.get("https://api.ipify.org?format=text").text}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
