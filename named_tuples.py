from collections import namedtuple

Point = namedtuple("Point","x y")
point = Point(2,4)
point.x 
point.y

params = {"x":2, "y":4}
point = Point(**params)

