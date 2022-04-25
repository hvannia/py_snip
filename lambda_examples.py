

items = {
    'laptop': lambda x: x * 600,
    'raspberry pi':lambda x: x * 5,
    'arduino': lambda x: x * 50
}

quantity = 4
value_of_laptop  = items['laptop'](quantity)
print(f"value of {quantity} laptops = ${value_of_laptop}")
value_of_raspi  = items['raspberry pi'](quantity)
print(f"value of {quantity} raspberry pi  = ${value_of_raspi}")

# lambda in list

[ (lambda x: x*3)(i) for i in range(5) ]
#[0, 3, 6, 9, 12]

list( map( (lambda x: x*3), range(5) ) )

