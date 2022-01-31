class Animal():
# main class 
    
     def __init__(self, name, age, skinType):
         self.name =  name
         self.age = age
         self.skinType = skinType.lower()
        
     def animal_type(self,skinType):
        if self.skinType == "fur":
            return "\n  If skin is fur , this  animal is a mamal."
       
        elif self.skinType == "feather":
            return "\n If skin is feather, this  animal is a bird." 
      
        else:
            return "\n Please enter feather or fur only." 
                
# Dog  class   
class Dog(Animal): 
     def __init__(self, name, age, skinType):
        super().__init__(name, age, skinType)
        
     def make_sound(self):
          return "\n Sound is woof."
        
# Lion class     
class Lion (Animal):
    def __init__(self, name, age, skinType):
        super().__init__(name, age, skinType)
        
    def lion_ways(self,age):
        if self.age < 3:
            return "\n This Lion is a cub."
        else:
             return "\n This is an adult lion." 
            
# Bird class 
class Bird(Animal):
    def __init__(self, name, age, skinType, fly):
        super().__init__(name, age, skinType)
        self.fly = fly.lower()
        
    def canFly(self,fly):
        if self.fly == "yes":
            return "\n This is a sky bird." 
        else:
            return "\n This is a land bird." 
            

#----------- Super  class ---------------           
'''
anmInfo = Animal("\n Bird", 2, "FUR") 
print( "Animal Type : " , anmInfo.name,
       "\n " +  "Age :" , anmInfo.age,
       "\n " + "Skin Type :", anmInfo.skinType.lower())
print(anmInfo.animal_type("")) '''

#----------- Dog class ---------------#
'''
dogIfo = Dog("Poddle ", 4, "black")
print(" Dog Type :", dogIfo.name,
       "\n " +  "Age :" , dogIfo.age,
       "\n " + "Fur Color : ", dogIfo.skinType)
print(dogIfo.make_sound())  '''

#----------- Lion class ---------------#
'''
lionInfo = Lion(" Male Lion ", 9 , " Grey")
print(" Animal Type : " , lionInfo.name,
       "\n " +  " Age :" , lionInfo.age,
       "\n " + " Fur Color:", lionInfo.skinType)
print(lionInfo.lion_ways(""))  '''


#----------- Bird class --------------- $ 
'''
birdInfo = Bird("Eagle ", 1 , "Green ", "YES")
print(" Bird Type : " , birdInfo.name,
       "\n " +  "Age :" , birdInfo.age,
       "\n " + "Feather Type : ", birdInfo.skinType, 
       "\n " + "Can it fly ? " , birdInfo.fly)
print(birdInfo.canFly("")) '''



