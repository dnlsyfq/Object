# class Dog:
    
#     sound = "Woof"
    
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
        
#     def bark(self):
#         print(Dog.sound)
        
        
# Dog('Roger',5).bark()



class Employee:
  new_id = 1

  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
      print(f"My id is {self.id}")
      

Employee().say_id()

Employee().say_id()