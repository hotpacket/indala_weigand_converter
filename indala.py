#!/usr/bin/python
import sys

def boolList2BinString(lst):
   return '0b' + ''.join(['1' if x else '0' for x in lst])

if (len(sys.argv) !=2 ) :
	print 'Usage: ./indala.py <wiegand value>'
	print 'Where <wiegand value> is the hex number read by the long range reader, e.g. 2007b8117a.'
	sys.exit()

wiegand = str(sys.argv[1])
print
print 'Converting Wiegand hex value', wiegand, 'to Indala format...'
try:
	wiegandhex = int(wiegand, 16)
except ValueError:
	print 'Not a valid hex value! Cannot convert.'
	sys.exit()
#print hex(wiegandhex)
wiegandbin = bin(wiegandhex)
#print 'Wiegand binary value:', str(wiegandbin)
wiegandbin = wiegandbin[-26:]
print 'Wiegand 26 bit binary value:', str(wiegandbin)

# Bit scrambling for Indala below. The details of the bit scrambling were found at
# http://www.proxmark.org/forum/viewtopic.php?id=624. This has only been tested
# on 26-bit Indala cards. The scrambling may be different on different bit lengths.

indala = [0,0,1,0,1,0,1]
#print indala
indala.insert(0,int(wiegandbin[22]))
indala.insert(0,int(wiegandbin[8]))
indala.insert(0,int(wiegandbin[1]))
indala.insert(0,int(wiegandbin[21]))
indala.insert(0,0)
indala.insert(0,int(wiegandbin[20]))
indala.insert(0,int(wiegandbin[6]))
indala.insert(0,int(wiegandbin[13]))
indala.insert(0,int(wiegandbin[16]))
indala.insert(0,int(wiegandbin[23]))
indala.insert(0,int(wiegandbin[2]))
indala.insert(0,int(wiegandbin[5]))
indala.insert(0,int(wiegandbin[4]))
indala.insert(0,int(wiegandbin[17]))
indala.insert(0,int(wiegandbin[10]))
indala.insert(0,int(wiegandbin[3]))
indala.insert(0,int(wiegandbin[11]))
indala.insert(0,int(wiegandbin[9]))
indala.insert(0,int(wiegandbin[24]))
indala.insert(0,int(wiegandbin[12]))
indala.insert(0,int(wiegandbin[7]))
indala.insert(0,int(wiegandbin[25]))
indala.insert(0,int(wiegandbin[19]))
indala.insert(0,int(wiegandbin[14]))
indala.insert(0,int(wiegandbin[15]))
indala.insert(0,int(wiegandbin[0]))
indala.insert(0,int(wiegandbin[18]))
indala.insert(0,1)

# --------------------------------
# The following code calculates the checksum according to the description in 
# http://www.proxmark.org/forum/viewtopic.php?id=624. HOWEVER, in my testing
# the checksum does not matter, either "10" or "01" for bits 30 and 31 produce 
# valid cards that grant access. If you read the thread, they are just guessing.
# Someone else mentioned that the values may be "00" or "11" in other implementations
# of Indala, but I found that those values produce invalid cards in my test of a normal
# Indala system. The best solution for now is to calculate the Indala value for all 
# four possible checksum values and present all to the user.

checksum = int(wiegandbin[10]) + int(wiegandbin[12]) + int(wiegandbin[15]) + int(wiegandbin[16])
checksum = checksum + int(wiegandbin[18]) + int(wiegandbin[19]) + int(wiegandbin[22]) + int(wiegandbin[24])  
if (checksum %2 == 0):
	print 'Checksum (',checksum,') is even. Adding \'10\' to bytes 30 and 31.'
	indala[30]=1
	indala[31]=0
	print
	print '--Candidate 1 (Try this one first)--'
	print 'Indala binary value:', bin(int(boolList2BinString(indala),2))
	print 'Indala hex value to write to card: %x' % int(boolList2BinString(indala),2)
	print
	print '--Candidate 2 (This will probably also work)--'
	indala[30]=0
	indala[31]=1
	print 'Indala binary value:', bin(int(boolList2BinString(indala),2))
	print 'Indala hex value to write to card: %x' % int(boolList2BinString(indala),2)
else:
        print 'Checksum (',checksum,') is odd. Adding \'01\' to bytes 30 and 31.'
	indala[30]=0
	indala[31]=1
        print
        print '--Candidate 1 (Try this one first)--'
        print 'Indala binary value:', bin(int(boolList2BinString(indala),2))
        print 'Indala hex value to write to card: %x' % int(boolList2BinString(indala),2)
        print
        print '--Candidate 2 (This will probably also work)--'
        indala[30]=1
        indala[31]=0
        print 'Indala binary value:', bin(int(boolList2BinString(indala),2))
        print 'Indala hex value to write to card: %x' % int(boolList2BinString(indala),2)
# --------------------------------

#print indala
#print 'Converted binary value:', bin(int(boolList2BinString(indala),2))

print
print 'Alternate Indala values to try if the above values do not work (these are only used in rare Indala configurations):'
indala[30]=0
indala[31]=0
#print 'Converted binary value:', bin(int(boolList2BinString(indala),2))
print '%x' % int(boolList2BinString(indala),2)
indala[30]=1
indala[31]=1
#print 'Converted binary value:', bin(int(boolList2BinString(indala),2))
print '%x' % int(boolList2BinString(indala),2)
