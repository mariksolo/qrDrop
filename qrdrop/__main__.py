from flask import Flask, send_file
import os
import socket
import click

app = Flask(__name__)

port = '5000'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect( ('8.8.8.8', 80) )
localip = s.getsockname()[0]
s.close()

@app.route('/')
def transfer_file():
    return send_file('pyproject.toml')

@click.command
def launch_file_transfer():
    click.echo('hello world')
    os.system('qrencode -t ansiutf8 "http://{}:{}"'.format(localip, port))
    app.run(host = '0.0.0.0')

if __name__ == '__main__':
    launch_file_transfer()

