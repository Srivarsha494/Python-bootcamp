class father:
     def  father_speak():
       return "father of kid"
class mother:
     def mother_speak():
          return "mother of kid"
class kid(father,mother):
    def kid_speak():
       return "i am child of father amd mother"
 
obj1=kid
print(obj1.father_speak())
print(obj1.mother_speak())
print(obj1.kid_speak())        