

class Letters():
    def __init__(self) -> None:
        self.x ='equis'
        self.y ='ye'
        self.z ='zeta'

# print all params in class
    def print_class_params(self):
        for attribute, value in self.__dict__.items():
            print(attribute, ' = ' ,value)

l= Letters()
l.print_class_params()