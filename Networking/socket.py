#created a socket

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.python.org',80))
s.send('test hello')
