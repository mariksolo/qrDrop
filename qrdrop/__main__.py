from flask import Flask, send_file
import os
import socket
import click
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

port = '5000'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect( ('8.8.8.8', 80) )
localip = s.getsockname()[0]
s.close()


@click.command
@click.argument('file', type=click.Path(exists=True, resolve_path=True))
def launch_file_transfer(file):
    click.echo('hello world')
    os.system('qrencode -t ansiutf8 "http://{}:{}"'.format(localip, port))

    @app.route('/')
    def transfer_file():
        click.echo("in transfer_file")
        click.echo(file)
        click.echo(click.format_filename(file))
        return send_file(click.format_filename(file))

    app.run(host = '0.0.0.0')

if __name__ == '__main__':
    launch_file_transfer()

