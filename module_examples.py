# python modules

#csv
#Read a css file w/o pandas

import csv

with open("Some_file.csv") as file_obj:
	reader = csv.reader(file_obj)
	for row in reader:
		print(row)

#sys
#What directories are searched when python imports a module or package
import sys
sys.path
#Where python executable is from 
sys.executable

#fake 
#Generating fake data
#python3 -m pip install Faker
from faker import Faker

fake.name()
fake.address()

fake_international = Faker(['it_IT','en_US','ja_JP'])
for _ in range(10):
	print(fake_international.name())

#fake python data 
fake.pyint()
fake.pylist()

#poplib
import poplib

mailbox.poplib.POP3('pop3.host.com')
mailbox.user("USERNAME")
mailbox.password("PASSWORD")
numMessages = len(mailbox.list()[1])
for i in range(numMessages):
	for j in mailbox.etr(i+1)[1]:
		print(j) 

#subprocess

import subprocess
output = subprocess.run(['ls','-l'], capture_output=True)
output.stdout



