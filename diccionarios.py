a_dict = {}
a_dict.setdefault("missing_key", "default value")
a_dict["missing_key"]

# if you call .setdefault() on an existing key, then the call won’t have any effect on the dictionary
a_dict.setdefault("missing_key", "another default value")  # still 'missing_key'


a_dict = {}
a_dict.get("missing_key", "default value")  # 'default value'
# value isn’t added to the underlying dictionary
a_dict  # {}


# union operations ( python 3.9 )
first = {"name": "Vannia", "occupation": "developer"}
second = {"location": "California", "hobby": "running, taekwondo, sewing"}
merged = first | second
merged


# mapping
scores = {"joe": 85, "jane": 90, "alex": 80, "beth": 82}
students = ["beth", "alex", "jane", "joe"]
# sort students by scores, highest first
sorted(students, key=scores.get, reverse=True)


from collections import defaultdict

issubclass(defaultdict, dict)  # True
"""
when you try to access or modify a key that’s not present in the dictionary, a default value is automatically given to that key
"""
# Grouping Items
dd = defaultdict(list)
dd["key"].append(1)
dd["key"].append(2)
dd["key"].append(3)
# defaultdict(list, {'key': [1, 2, 3]})
dep = [
    ("Sales", "John Doe"),
    ("Sales", "Martin Smith"),
    ("Accounting", "Jane Doe"),
    ("Marketing", "Elizabeth Smith"),
    ("Marketing", "Adam Doe"),
]
dep_dd = defaultdict(list)
for department, employee in dep:
    dep_dd[department].append(employee)
# defaultdict(list,
# 			   {'Sales': ['John Doe', 'Martin Smith'],
#             'Accounting': ['Jane Doe'],
#             'Marketing': ['Elizabeth Smith', 'Adam Doe']})


# use a set as the .default_factory to avoid duplicates
dep = [
    ("Sales", "John Doe"),
    ("Sales", "Martin Smith"),
    ("Accounting", "Jane Doe"),
    ("Marketing", "Elizabeth Smith"),
    ("Marketing", "Elizabeth Smith"),
    ("Marketing", "Adam Doe"),
    ("Marketing", "Adam Doe"),
    ("Marketing", "Adam Doe"),
]

dep_dd = defaultdict(set)
for department, employee in dep:
    dep_dd[department].add(employee)

# Accumulating values
incomes = [
    ("Books", 1250.00),
    ("Books", 1300.00),
    ("Books", 1420.00),
    ("Tutorials", 560.00),
    ("Tutorials", 630.00),
    ("Tutorials", 750.00),
    ("Courses", 2500.00),
    ("Courses", 2430.00),
    ("Courses", 2750.00),
]

dd = defaultdict(float)
for product, income in incomes:
    dd[product] += income

for product, income in dd.items():
    print(f"Total income for {product}: ${income:,.2f}")

# passing Arguments to .default_factory.
# [Passing Arguments to defaultdict – Real Python](https://realpython.com/lessons/passing-arguments/)


def factory(arg):
    # Do some processing here...
    result = arg.upper()
    return result


def_dict = defaultdict(lambda: factory("default value"))
def_dict["missing"]
# if you try to access or modify a missing key -> 'DEFAULT VALUE'


# sort list of dict - do not mutate it
animals = [
    {"type": "cat", "name": "Stephanie", "age": 8},
    {"type": "dog", "name": "Devo", "age": 3},
    {"type": "rhino", "name": "Moe", "age": 5},
]
sorted(animals, key=lambda animal: animal["age"])

# actually chnage the list
animals.sort(key=lambda animal: animal["age"])


from collections import defaultdict

# another example

# add default values
student_grades = defaultdict(list, {"Ivan": [90, 80, 70], "Hugo": [90, 90, 90]})
# add default value w lambda
student_score = defaultdict(lambda: 75)
student_score["Erick"] += 10
