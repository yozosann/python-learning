import socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.settimeout(1)
try:
  sk.connect(('ubuntu@ec2-18-220-102-128.us-east-2.compute.amazonaws.com',80))
  print('Server port 80 OK!')
except Exception:
  print('Server port 80 not connect!')
sk.close()