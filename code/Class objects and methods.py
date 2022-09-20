#Class objects and methods

class Person:
    name=""
    
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def greet(self):
        return "Hello {}".format(self.name)


p=Person()

print(p.name)
p.setName("Vaibhav")
print(p.name)
p.setName("Ri")
print(p.name)

p2=Person()

print(p2.name)
p2.setName("Ha")
print(p2.name)
p2.setName("Hp")
print(p2.name)



