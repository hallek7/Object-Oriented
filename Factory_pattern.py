from abc import ABC, abstractmethod
class Hotel(ABC): # Hotel
  
   @abstractmethod
   def hotelInfo(self): #hotel Info
         pass
        
## ----------------------------Hotel  people ----------------------------

class Hotel_people(ABC): # Hotel_people  
    
      @abstractmethod
      def hotelInfo(self): # hotelInfo
          pass
        
class Hotel_employee(Hotel_people): #Hotel_employee  
    
    def hotelInfo(self): # hotelInfo
        return 'hotel employee  info and job coming soon'
    
class Hotel_customer(Hotel_people): # Hotel_customer 
    
    def hotelInfo(self):  # hotelInfo
        return 'hotel customer actions and info goes here'
    

## ---------------------------- Hotel Rooms ----------------------------
class Hotel_roomA(Hotel): # Hotel_roomA  
    
      def hotelInfo(self): #hote lInfo
          return 'Hotel room A is under construction'
        

class Hotel_roomB(Hotel): # Hotel_roomB  
      def hotelInfo(self):  
           return  'Hotel room B is also under construction'
        
    
class Hotel_factory(ABC): # Hotel_factory  
    
     @abstractmethod
     def createRooms(self): # createRooms  
         pass
    
     @abstractmethod
     def createPeople(self): #createPeople  
          pass
        
class People_factory(Hotel_factory): # People_factory  
    
     def createPeople(self): #createPeople   
         return Hotel_employee()
        
     def createPeople(self):  
         return Hotel_customer() # change hotel rooms Hotel_roomB() or Hotel_roomA()
        
     def createRooms(self):   #createRooms   
         return Hotel_roomB() # change to Hotel_roomA() or 
        
 
class Rooms_factory(Hotel_factory): # Rooms_factory
     
     def createPeople(self):  
         return Hotel_customer() # change hotel rooms Hotel_roomB() or Hotel_roomA()
 
     def createPeople(self):  
         return Hotel_employee()
        
     def createRooms(self):  
         return Hotel_roomA()
        
  
if __name__ == "__main__":   
    factory = People_factory()    # People_factory() = createRooms() 
    rooms = factory.createRooms() # Rooms_factory() =  createPeople()
    print(rooms.hotelInfo())  
        

 
 

