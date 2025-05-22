
### Object
```
def __init__(self):
  self.attribute = Class_Name.class_variable
  Class_Name.class_variable += 1
```

```
class Employee:
  new_id = 1

  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
      print(f"My id is {self.id}")
      

Employee().say_id() // 1

Employee().say_id() // 2
```

### Inheritance

```
class ParentClass:
  #class methods/properties...

class ChildClass(ParentClass):
  #class methods/properties...

```

```
class Animal: 
  def eat(self): 
    print("Nom Nom Nom...eating food!")

class Dog(Animal):
  def bark(self):
    print('Bark!')

class Cat(Animal):
  def meow(self):
    print('Meow!')

fluffy = Dog()
zoomie = Cat()

fluffy.eat() # Nom Nom Nom...eating food!
zoomie.eat() # Nom Nom Nom...eating food!

```
```
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

# Write your code below
class Admin(Employee):
  pass

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()
```

### Overriding
 a child class may want to change the behavior of a method from its parent class. In Python, all we have to do is override a method definition. An overriding method in a subclass is one that has the same definition as the parent class but contains different behavior.

```
class Animal:
  def __init__(self, name):
    self.name = name

  def make_noise(self):
    print("{} says, Grrrr".format(self.name))

pet1 = Animal("Rex")
pet1.make_noise() # Rex says, Grrrr

class Cat(Animal):

  def make_noise(self):
    print("{} says, Meow!".format(self.name))

pet2 = Cat("Maisy")
pet2.make_noise() # Maisy says, Meow!

```

### super()
When overriding methods we sometimes want to still access the behavior of the parent method. In order to do that we need a way to call the method of the parent class. Python gives us a way to do that using 
Preview: Docs Loading link description
super()
.

super() gives us a proxy object. With this proxy object, we can invoke the method of an object’s parent class (also called its superclass). We call the required function as a method on super()

