from socket import *
srv = '172.16.85.98' # server ip add.
srvPt = 54111
clntSkt = socket(AF_INET, SOCK_DGRAM)
msg = raw_input('Enter the data : ')
clntSkt.sendto(msg,(srv, srvPt))
msg, srvAddr = clntSkt.recvfrom(2048)
print msg
clntSkt.close()
