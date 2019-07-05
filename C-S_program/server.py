# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 17:28:40 2017

@author: Administrator
"""
#!/usr/bin/python
from Auto_data import ht_connect
from Auto_data import data_export
import socket, threading
import time
import json
def get_data(s,addr):
      while True:
            request=json.loads(s.recv(4096).decode())
            if request[0]=='数据请求':
                  print(request[1]+request[2])
                  break
      try:
            data=data_export(ht_connect(request[4]),request[3])
            cnt=len(data)
      except:
            data=[]
            cnt=0

      s.send(json.dumps(['数据条数',str(len(data))]).encode())
      while True:
            if json.loads(s.recv(4096).decode())[0]=='条数确认':break
      for x in data:
            s.send(json.dumps(['数据',[x]]).encode())
            while True:
                  if json.loads(s.recv(4096).decode())[0]=='确认':break
      s.send(json.dumps(['提示',request[1]+'.'+request[2]+'传输结束']).encode())
      print ('Connection from %s:%s closed' % addr)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('', 140))
s.listen(5)
print ('Waiting for connection...')

while True:
      sock, addr = s.accept()
      print ('Connection from %s:%s ' % addr)
      sock.send(json.dumps(['提示','Welcome!']).encode())
      # 建立一个线程用来监听收到的数据
      #get_data(sock, addr)
      t = threading.Thread(target = get_data, args = (sock, addr))
      # 线程运行
      t.start()
