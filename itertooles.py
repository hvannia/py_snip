import itertools as it

all_ones = it.repeat(1)
next(all_ones)  # returns 1 no matter how manytimes its called
# don't call list on all_ones because it will return infinity


list(map(pow, range(10), it.repeat(2))) )  # squared 0 to 9 
#  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# finite number of 1's:
all_ones=it.repeat(1, times = 5)
list(all_ones)
# [1, 1, 1, 1, 1]

# cycle will go on forever
alternating_ones = it.cycle([1,-1])
next(alternating_ones)  # 1
next(alternating_ones)  # -1 
next(alternating_ones)  # 1
next(alternating_ones)  # -1 

# find all permutations of a specific length
mboys=["ivan","hugo","Erick"]  
it.permutations(mboys, r=2)  #length 2
list(it.permutations(mboys, r=2))
"""
[('ivan', 'hugo'),
 ('ivan', 'Erick'),
 ('hugo', 'ivan'),
 ('hugo', 'Erick'),
 ('Erick', 'ivan'),
 ('Erick', 'hugo')]"""
list(it.permutations(mboys, r=3))
"""[('ivan', 'hugo', 'Erick'),
 ('ivan', 'Erick', 'hugo'),
 ('hugo', 'ivan', 'Erick'),
 ('hugo', 'Erick', 'ivan'),
 ('Erick', 'ivan', 'hugo'),
 ('Erick', 'hugo', 'ivan')]
 """

# combinations
list(it.combinations(mboys, r=3))
#  [('ivan', 'hugo', 'Erick')]












# from itertools import chain

# my_list = ['foo','bar']
# numbers = list(range(5))
# cmds = ['ls','/some/dir']
# my_list = list(chain(['foo','bar'], cmds, numbers))

# # all posssible roles of 3 dice
# rolls = itertools.product(range(1,7), repeat =3)
# tally = collections.Counter(sum(t) for t in rolls))
# for total in sorted(tally):
#     occurs = tally[total]
#     print(f"{total:3d}: {occurs:3d} {'░'*occurs}▍")