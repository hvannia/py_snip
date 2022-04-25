num = 10_000_000
print(f"{num:,}")

# fil numbers
for i in range(1,3): # num 1-2
    str(i).zfill(3)
'''
001
002
'''    

# chained comparison
heart_rate = 85 
if 60 < heart_rate and heart_rate < 100:
    print("good hr")
if 60 <  heart_rate < 100:
    print("good hr")

# ternary 
condition = True
x =1 if condition else 0


# zip
names = ['Peter','Clark','Wade','Bruce']
heroes = ['Spiderman','Superman','Deadpool','Batman']
universes = ['Marvel','DC','Marvel','DC']

for name, hero, universe in zip(names,heroes,universes):
    print(f'{name} is actually {hero} in {universe}')


#unpacking
a,b,*_ = (1,2,3,4,5)
print(a)
print(b)
a,b,*c = (1,2,3,4,5)
print(a)
print(b)
print(c)

#printing values
name = "Mike"
#old
f"name={name}"
# new syntax
f"{name=}"

# 
concat = "".join
concat(["ab","cd","ef","!"])
