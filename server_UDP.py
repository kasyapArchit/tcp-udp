from socket import *
srvPt = 54111
srvSkt = socket(AF_INET, SOCK_DGRAM)
srvSkt.bind(('',srvPt))
print "The server is ready to receive"
while 1:
	msg, cltAddr = srvSkt.recvfrom(2048)
	print 'message received'
	#lst = map(str,msg.split())
	rslt = list(msg)
	rslt.sort()
	msg = "".join(str(x) for x in rslt)
	srvSkt.sendto(msg, cltAddr)