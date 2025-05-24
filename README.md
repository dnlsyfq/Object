
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
When overriding methods we sometimes want to still access the behavior of the parent method. In order to do that we need a way to call the method of the parent class. 

super() gives us a proxy object. With this proxy object, we can invoke the method of an object’s parent class (also called its superclass). We call the required function as a method on super()

```
class Animal:
  def __init__(self, name, sound="Grrrr"):
    self.name = name
    self.sound = sound

  def make_noise(self):
    print("{} says, {}".format(self.name, self.sound))

class Cat(Animal):
  def __init__(self, name):
    super().__init__(name, "Meow!") 

pet_cat = Cat("Rachel")
pet_cat.make_noise() # Rachel says, Meow!

```

```
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    # Write your code below:
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()

```

### Multiple Inheritance

```
class Animal:
  def __init__(self, name):
    self.name = name
 
  def say_hi(self):
    print("{} says, Hi!".format(self.name))

class Cat(Animal):
  pass

class Angry_Cat(Cat):
  pass

my_pet = Angry_Cat("Mr. Cranky")
my_pet.say_hi() # Mr. Cranky says, Hi!

```

```
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

# Write your code below
class Manager(Admin):
  def say_id(self):
    print("We are ub charge.")
    super().say_id()


e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()
e4.say_id()
```

```
class Animal:
  def __init__(self, name):
    self.name = name

class Dog(Animal):
  def action(self):
    print("{} wags tail. Awwww".format(self.name))

class Wolf(Animal):
  def action(self):
    print("{} bites. OUCH!".format(self.name))

class Hybrid(Dog, Wolf):
  def action(self):
    super().action()
    Wolf.action(self)

my_pet = Hybrid("Fluffy")
my_pet.action() # Fluffy wags tail. Awwww
                # Fluffy bites. OUCH!

```

```
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))

# Write your code below
class Admin(Employee, User):
  def __init__(self):
    super().__init__()
    User.__init__(self,self.id,"Admin")
    

  def say_id(self):
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()

```

### Polymorphism
polymorphism is the ability to apply an identical operation onto different types of objects. 

```
class Animal:
  def __init__(self, name):
    self.name = name

  def make_noise(self):
    print("{} says, Grrrr".format(self.name))

class Cat(Animal):

  def make_noise(self):
    print("{} says, Meow!".format(self.name))

class Robot:
  
  def make_noise(self):
    print("beep.boop...BEEEEP!!!")



an_animal = Animal("Bear")
my_pet = Cat("Maisy")
my_vacuum = Robot()
objects = [an_animal, my_pet, my_vacuum]
for o in objects:
  o.make_noise()

# OUTPUT
# "Bear says, Grrrr"
# "Maisy says, Meow!"
# "beep.boop...BEEEEP!!!"

```

```
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge!")

# Write your code below
meeting = [Employee(),Admin(),Manager()]

for o in meeting:
  o.say_id()
```