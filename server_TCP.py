from socket import *
srvPt = 29003
srvSkt = socket(AF_INET, SOCK_STREAM)
srvSkt.bind(('',srvPt))
srvSkt.listen(1)
print 'Ready to receive'
while 1:
	ctnSkt, addr = srvSkt.accept()
	msg, null = ctnSkt.recvfrom(1024)
	print 'Message received'
	lst = map(int, msg.split())
	lst.sort()
	lst.reverse()
	msg = " ".join(str(x) for x in lst)
	print msg
	ctnSkt.send(msg)
	ctnSkt.close()
