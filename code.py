import time
from socket import *

line = ""
with open('data.txt') as f:
	line= f.readlines()

date = int(time.strftime("%d"))
month = int(time.strftime("%m"))
if (month == 6):
	date = date + 31

ramadanHariKe = date-16

jadwal = line[ramadanHariKe].split()
jadwalshalat = []
jadwalshalat.append(jadwal[1])
jadwalshalat.append(jadwal[4])
jadwalshalat.append(jadwal[5])
jadwalshalat.append(jadwal[6])
jadwalshalat.append(jadwal[7])

jadwalshalat_mm = []
for x in jadwalshalat:
	temp = x.split(":")
	h = int(temp[0])
	m = int(temp[1])
	mm = (h*60) + m
	jadwalshalat_mm.append(mm)


shalat = []
shalat.append("Subuh")
shalat.append("Zuhur")
shalat.append("Asar")
shalat.append("Magrib")
shalat.append("Isya")

now_h = int(time.strftime("%H"))
now_m = int(time.strftime("%M"))
now_mm = (now_h*60) + now_m
#print now_mm
print  str(now_h)+ ':'+str(now_m)

#now_mm = 712

marker = 0
for x in jadwalshalat_mm:
	if now_mm > x:
		marker = marker + 1

str_ramadhan = str(ramadanHariKe) + " Ramadhan 1439 H"
str_shalatselanjutnya = ""

if (marker <= 4):
	print str(shalat[marker]) + ' : ' + str(jadwalshalat[marker])
	selisih = jadwalshalat_mm[marker] - now_mm
	jam = selisih / 60
	menit = selisih % 60
	print str(jam) + ' Jam ' + str(menit) + ' Menit'
else:
	jadwal = line[ramadanHariKe+1].split()
	jadwalshalat = []
	jadwalshalat.append(jadwal[1])
	jadwalshalat_mm = []
	for x in jadwalshalat:
		temp = x.split(":")
		h = int(temp[0])
		m = int(temp[1])
		mm = (h*60) + m
		jadwalshalat_mm.append(mm)

	selisih = jadwalshalat_mm[0] + (1440-now_mm)
	jam = selisih / 60
	menit = selisih % 60
	print str(ramadanHariKe) + " Ramadhan 1439 H"
	print str(jam) + ' Jam ' + str(menit) + ' Menit menuju ' + str(shalat[0]) + ' (' + str(jadwalshalat[0]) + ')'
	str_shalatselanjutnya = str(jam) + ' Jam ' + str(menit) + ' Menit menuju ' + str(shalat[0]) + ' (' + str(jadwalshalat[0]) + ')'


str_ramadhan 
str_shalatselanjutnya

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.bind(('localhost',8080))
    serversocket.listen(5)
    while(1):
        (clientsocket, address) = serversocket.accept()
        data = clientsocket.recv(2048)
        print data
        clientsocket.send("HTTP/1.1 200 OK\n"
         +"Content-Type: text/html\n"
         +"\n" # Important!
         +"<html><body>"
         +str_ramadhan
         +"<br>"
         +str_shalatselanjutnya
         +"</body></html>\n")
        clientsocket.shutdown(SHUT_WR)
        clientsocket.close()
    serversocket.close()

createServer()
