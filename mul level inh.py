class animal:
     def speak():
       return "i am speaking"
class dog(animal):
     def bark():
          return "bow...."
class puppy (dog):
    def shout():
        return "i am child of dog"
 
obj1=puppy
print(obj1.speak())
print(obj1.bark())
print(obj1.shout())     