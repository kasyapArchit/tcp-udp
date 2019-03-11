from socket import *
srv = '172.16.85.98' # use server ip add.
srvPt = 29003
clntSkt = socket(AF_INET, SOCK_STREAM)
clntSkt.connect((srv, srvPt))
msg = raw_input('Enter the data : ')
clntSkt.send(msg)
ansr, null = clntSkt.recvfrom(1024)
print ansr
clntSkt.close()
