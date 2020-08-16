#!/usr/bin/python3

import re
import sys

class Vcard:
	'This class is a contact VCARD 2.1'
	total_vcards = 0
	
	def __init__(self, firstn, lastn, essential):
		self.firstn = firstn
		self.lastn = lastn
		self.nums = []
		self.essential = essential
		self.card =[]
		Vcard.total_vcards +=1
	def displayCount(self):
		print("Total Cards %d" % Vcard.total_vcards)
	def addnum(self, num):
		self.nums.append(num)
	def displayVcard(self):
		print("BEGIN:VCARD\nVERSION:2.1")
		print("N:%s;%s" % (self.lastn,self.firstn))
		print("FN:%s %s" % (self.firstn,self.lastn))
		if len(self.nums) != 0:
			for i in range(len(self.nums)):
				if i == 0:
					print("TEL;CELL;PREF:%s" % (self.nums[i]))
				else:
					print("TEL;CELL:%s" % (self.nums[i]))
		print("END:VCARD")
	def displaycsv(self):
		print("%s" % (self.firstn), end=";")
		print("%s" % (self.lastn), end=";")
		#print("%d" % (self.essential), end=";")
		if len(self.nums) != 0:
			for i in range(len(self.nums)):
					print("%s" % (self.nums[i]), end=";")
		print("")


###OPEN File####
file_vcf = str(sys.argv[1])

try:
   file = open(file_vcf, "r")

except IOError:
   print ("There was an error reading file")
   sys.exit()

input_vcf = [line.rstrip('\n') for line in file]

file.close()

firstn= str()
lastn= str()
num= str()

contacts = []

for index in range(len(input_vcf)):

	if re.match("BEGIN:VCARD",input_vcf[index]):
		del firstn,lastn,num
		firstn= str()
		lastn= str()
		num= str()
	if re.match("N",input_vcf[index]):
		temp = re.sub(r'^.*:', "",input_vcf[index])
		#Cut anything after first ;
		lastn = re.sub(r';.*$', "",temp)
		#Cut first and all ; from temp
		firstn= re.sub(r'\W',"",re.sub(lastn,"",temp))
		contacts.append(Vcard(firstn, lastn, "N/A"))
	if re.match("TEL",input_vcf[index]):
		temp = re.sub(r'^.*:', "",input_vcf[index])
		contacts[-1].addnum(temp)


for index in range(len(contacts)):
	contacts[index].displaycsv()
		
		

		
	
		
