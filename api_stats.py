#from collections import defaultdict

# setup, a bunch of  api params and values

DATA = [
	{"body": {"name":"groceries", "category" : "nourishment", "date":"2020-06-18", "exp_in":1, "ammount": 171}, 
	 "r_time": 171 	},
	{"body": {"name":"food", "category" : "pet", "date":"2020-06-15", "exp_in":1, "ammount": 25},
	  "r_time":  100 },
	{"body": {"name":"medical", "category" : "pet", "date":"2020-05-15", "exp_in":1, "ammount": 275},
	 "r_time":  200 },
	{"body": {"name":"deposit", "category" : "paycheck", "date":"2020-06-14", "exp_in":0, "ammount": 525},
	 "r_time":  525},
	{"body": {"name":"deposit", "category" : "paycheck", "date":"2020-06-14", "exp_in":0, "ammount": 25},
	 "r_time":  25 }
]

# p_amounts=[]
# p_times=[]
PATTERNS =[ {"name": "pet expense",
			"values": [ {"exp_in":1} , { "category":"pet"} ] ,
			"count" : 0,
			},
			{"name": "income",
			"values": [ {"exp_in":0} , { "category":"paycheck"} ] ,
			"count" : 0,
			}  ]

#p1=PATTERNS[0]['values']

for d in DATA:
	#print(f'{d[0]}')
	matches = []
	for pattern in PATTERNS:
		p_values = pattern['values']
		for p in p_values:
			print(p)
			k = list(p.keys())[0]
			v = list(p.values())[0]
			body = d['body']
			matches.append(body.get(k,False)==v)	
			#print(f'pattern : {p} in {d}: {body.get(k,None) == v} \n')#{p in d[0]}')
		all_matches=True;
		for m in matches:
			all_matches = all_matches and m
		p_amounts = pattern.get('amounts',[])
		p_times = pattern.get('r_time',[])
		if all_matches:
			print(f'match for input {d["body"]}: ')
			pattern['count'] = pattern['count']+1
			p_amounts.append(d['body']['ammount'])	
			p_times.append(d['r_time'])
			pattern['amounts'] = p_amounts
			pattern['times'] = p_times

#next muplify and boxplotify

for p in PATTERNS:
	print(p)
