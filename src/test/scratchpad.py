class Person:
    def __init__(self,name,last):
        self.name = name 
        self.last = last

    def cost(self):
        pass

    def test(self):
        pass

obj = Person("manish","kumar")

print(dir(obj))