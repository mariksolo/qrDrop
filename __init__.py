from flask import Flask, send_file
import os
import socket

app = Flask(__name__)

@app.route('/')
def transfer_file():
    return send_file('pyproject.toml')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect( ('8.8.8.8', 80) )
localip = s.getsockname()[0]
s.close()

port = '5000'

os.system('qrencode -t ansiutf8 "http://{}:{}"'.format(localip, port))

app.run(host = '0.0.0.0')
