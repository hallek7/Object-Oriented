class Hotel(object):
    
   def hotel_funcations(self):
       self.employeeA = EmployeeA()
       self.employeeA.night_employee()
     
       self.customer = CustomerA()
       self.customer.customerA_info()
      
       self.roomA  = RooomA()
       self.roomA.roomA_info()
     

class EmployeeA (object):
    
     def night_employee(self):
         print ('Employee A  works over night')
     
     
class CustomerA(object):
    
    def customerA_info(self):
        print ('Employee A  checks in customers and answer questions')
    

class RooomA(object):
    
      def roomA_info(self):
          print ('Room A information goes here')
         
 
if __name__ == "__main__" :
  hotel = Hotel()
  hotel.hotel_funcations()

 
    
 




 
