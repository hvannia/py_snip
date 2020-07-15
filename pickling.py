# exmple of pickle from "The quick python book" pg 183

import pickle

def save_data():
	global a,b,c 
	file = open("state",'wb')
	data = {'a':a, 'b':b, 'c':c }
	pickle.dump(data,file)
	file.close()

def restore_data():
	global a,b,c
	file = open("state",'rb')
	data = pickle.load(file)
	file.close()
	a = data['a']
	b = data['b']
	c = data['c']
