## Difference between the staticmethod, @classmethod and @property decorators

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # A static method is a method that belongs to the class and not to the instance of the class. 
    # It can be called on the class itself, rather than on an instance of the class.
    @staticmethod
    def my_static_method():
        print("I am a static method!")

    #  method that belongs to the class and not to the instance of the class.
    #  It can be called on the class itself, rather than on an instance of the class.
    @classmethod
    def my_class_method(cls):
        print("I am a class method!")

    # define a method as a property of a class. 
    # A property is a method that is accessed like an attribute, without parentheses.
    @property
    def my_property(self):
        print("I am a property!")

# Create an instance of MyClass
my_instance = MyClass(1, 2)

# Call the static method
my_instance.my_static_method()

# Call the class method
my_instance.my_class_method()

# Call the property
my_instance.my_property

