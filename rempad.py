gbs = open("bin/hUGEGBS.gbs","rb")
length = len(gbs.read())-0x400
gbs.seek(0)
buffer = [0]*length

i = 0
while gbs.tell()-0x400 < length:
	if gbs.tell() < 0x70 or gbs.tell() > 0x46F:
		buffer[i] = int.from_bytes(gbs.read(1), "big")
		i += 1
	else:
		gbs.read(1)
gbs.close()
out = open("bin/hUGEGBS.gbs","wb")
out.write(bytearray(buffer))
out.close()