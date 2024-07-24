class animal:
     def speak():
       return "i am speaking"
class dog(animal):
     def  speak():
          return "bow...."
class puppy (dog):
    def speak():
        return "i am puppy"
 
obj1=puppy
print(obj1.speak())