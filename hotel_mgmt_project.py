import sqlite3
import random
conn = sqlite3.connect('hotel.db')

c = conn.cursor()
 
 # ==================== create object/tables ==========================# 
# c.execute("""
#  CREATE TABLE hotel (
#     hoteld integer PRIMARY KEY,
#     hotel_name  text NOT NULL,
#     city text NOT NULL, 
#     state text NOT NULL, 
#     employeeId integer ,
#     FOREIGN KEY (employeeId) REFERENCES employees (empId)
#   )""")
 
# c.execute("""
#  CREATE TABLE employees (
#     empId integer PRIMARY KEY,
#     first_name  text NOT NULL,
#     last_name text NOT NULL, 
#     salary  integer
#   )""")
 #------------------------------------------
# c.execute("""
#  CREATE TABLE guests (
#     id integer PRIMARY KEY,
#     first_name  text NOT NULL,
#     last_name text NOT NULL, 
#     roomNo integer ,
#     checkin  varchar ,
#     checkout varchar ,
#     FOREIGN KEY (roomNo) REFERENCES rooms (roomId)
#   )""")
 #------------------------------------------
# c.execute("""
#  CREATE TABLE rooms (
#     roomId integer PRIMARY KEY,
#     price  text NOT NULL,
#     num_of_beds  integer
#   )""")
 #------------------------------------------
# def create_employees(con, first_name, last_name, ):
#     sql = """
#         INSERT INTO Eml (first_name, last_name)
#         VALUES (?, ?)"""
#     cur = con.cursor()
#     cur.execute(sql, (first_name, last_name))
#     return cur.lastrowid
 
class Hotel:
    
       def hotel_info():
            state = input(" Which state are you coming from : " ).lower()        
            city = input(" What city ? : ").lower()
         
            print( city , state , " sounds like an awesome place ")
            hotl =  """ SELECT * FROM  hotel"""
            c = conn.cursor()
            c.execute(hotl)
            hotrows = c.fetchall()
            for htl in hotrows:
              print(" Welcome to hotel : ", htl)
      
         
class Room():
    
    def room_info():
       print (" Hotel Transylvania: Transformania has various rooms with upto " + 
        " 23 beds " )
       rom = " SELECT * FROM  rooms"
       c.execute(rom)
       rows = c.fetchall()
       for room in rows:
        print(" \n Room No, Price, and Number of beds ", room) 
        
 
class Restaurant():
    def showRest():    
        print("\n Resaurant is currently not in service ")
   

class Restaurant_employee(): 
    
     def restEmp():
        emp2 = " SELECT first_name, last_name FROM employees LIMIT 3 "
        c.execute(emp2)
        rows = c.fetchall()
        for emp in rows:
           print("\n Restaurant_employee ", random.choice(emp))
  
      

         
class Hotel_employees():
    
    def allEmp_info():
       empz = "SELECT * FROM  employees"
       c.execute(empz)
       rows = c.fetchall()
       for emp in rows:
           print(" \n These are the list of employees at the hotel ", emp)
        
class Guests:
    
    def guest_info():
        guest = "SELECT * FROM  guests"
        c.execute(guest)
        rows = c.fetchall()
        for hotelx in rows:
            print(" \n Rooms Info(room no, price, number of beds) ", hotelx)

#------------------------------------ methods create objects into DB ----------------------------------------      
 # 1 ================ employee function ===================#
def new_employee():  
    emp = []
    first_name = input(" Enter first name :" )
    emp.append(first_name)
    last_name = input(" Enter last name : " )
    emp.append(last_name)
    salary = input(" Enter your salary : " )
    emp.append(salary)
    empl = (emp)
    addEmp ="INSERT  into employees (first_name,last_name,salary)values(?,?,?)"
    c.execute(addEmp,empl)
    conn.commit ()
    print(' Welcome to work ')
    
def create_hotelGuests(conn, id, first_name, last_name, roomNo, checkin, checkout):
    sql =  """ INSERT INTO guests (id, first_name, last_name, roomNo, checkin, checkout)
        VALUES (?, ?, ?, ?, ?, ?)"""
    c = conn.cursor()
    c.execute(sql,(id, first_name, last_name, roomNo, checkin, checkout))
    return c.lastrowid   
    
def create_rooms(conn, roomId, price, num_of_beds):
    room =  """ INSERT INTO rooms (roomId, price, num_of_beds)
        VALUES (?, ?, ?)"""
    c = conn.cursor()
    c.execute(room,(roomId, price, num_of_beds))
    return c.lastrowid   
     
def create_hotel(conn, hotel_name, city, state, employeeId):
    hotel =  """ INSERT INTO hotel ( hotel_name, city, state, employeeId)
        VALUES (?, ?, ?, ?)"""
    c = conn.cursor()
    c.execute(hotel,( hotel_name, city, state, employeeId))
    return c.lastrowid  
     
 #--------------------------- make_reservation ------------------------------------# 
def make_reservation():
    guest = []
    first_name = input("Enter first name : " )
    guest.append(first_name)
    last_name = input(" Enter last name : " )
    guest.append(last_name)
   # try:
    checkin = input("Enter checkin date(mm/dd/yy) : " )
    guest.append(checkin)
    checkout = input("Enter checkout  date (mm/dd/yy) : " )
    guest.append(checkout)
    #except ValueError:
       # print("invlid entry or format")
    gst = (guest)
    inserIntoGuest = " INSERT  INTO guests(first_name, last_name,checkin, checkout)VALUES(?,?,?,?) " 
    c.execute(inserIntoGuest, gst)
    conn.commit ()

   
def selectRoom():
      print (" \n Hotel Transylvania: Transformania has various rooms with " + 
              " 1- 23 bed to accomidate all your needs")
      print("------------------------------------------------------")
      print( " Do you want to see room type available : Enter 1 for yes : ")
      ch=int(input("Enter your choice : "))
      if ch==1:
         rm = "SELECT * FROM  rooms"
         c.execute(rm)
         rows = c.fetchall()
         for x in rows:
             print(x)
      else:
       print ('OK, have a nice day')
                
def roomsPrice():
        print("\n We have the following rooms for you : ")
        print(" Rm ", 3, " Prince:",150," Num of beds : ", 23)
        print(" Rm ", 5, " Prince:",70, " Num of beds : ", 2)
        print(" Rm ", 6, " Prince:",87, " Num of beds : ", 4)
        print(" Rm ", 7, " Prince:",55, " Num of beds : ", 1)
        print(" Rm ", 8, " Prince:",100," Num of beds : ", 3)
        print(" Rm ", 9, " Prince:",120," Num of beds : ", 2)
       
        try:
          choose = int(input("Enter Your Room Number : "))
          nights = int(input("For How Many Nights : "))
        except ValueError:
            print(" please numers listed above ")
            
        if (choose == 3):
            result = 150 * nights
        elif (choose == 5):
             result = 70 * nights
        elif (choose == 6):
             result = 87 * nights
        elif (choose == 7):
             result = 55 * nights
        elif (choose == 8):
             result = 100 * nights
        elif (choose == 9):
             result = 120 * nights
             
        else:
            print (" Please pick a room ")
            
        print ("you've choosen room : ", choose , " \n",  " It costs : ", result ," a night " , "\n")
                 
def cancel_reservation():
    cncl = input(" \n Do you wish to cacel reservation ? enter 1 for yes 2 for no : ")
    checkIndate = input("Days remaining before your checkin ? (enter numbers) : ") 
    if (cncl == 1 and checkIndate < 3 ):
        print("Sorry you can't cancel reservation anymore ")
    elif(cncl == 1 and checkIndate > 3):
         print(" You'll get full refund in 5-7 business days ")
    else:
        print(" We're looking forward to seeing you ")
    #--------- I couldn't get line 221 -224 to execute :( 
    
def show_results():
    Hotel.hotel_info() 
    Room.room_info()
    Restaurant.showRest()
  
#------------ data for hotel  staff------------#
    print(" \n Please enter a numbers 1 -5  to see : ")
    print(" 1 all  employes detail ")
    print(" 2  restaurant employee info")
    print(" 3  new employee info  ")
    print(" 4  rooms ")
#__________________________ data for staff and guest  ____________# 
    print(" 5 new reservation (staff and guest)")
    # print(" Room  Price ")
    # print(" Selected Room " )
    # print(" Hotel guest information ")
    # print(" Guest bill ")
       
    try:
        userinput=int(input(" please select listed option : "))
    except ValueError:
        exit(" Enter  numeric values  only ")   
        
    if(userinput== 1):
        Hotel_employees.allEmp_info()
    elif(userinput == 2):
        Restaurant_employee.restEmp()
        
    elif(userinput == 3):
        new_employee() 
    
    elif(userinput == 4):
        Room.room_info()
        
    elif(userinput == 5):
        make_reservation()
        selectRoom()
        roomsPrice()     
    else:
      print("looks like you're trying to cancel or view reservations ",  cancel_reservation())
       
 
show_results()

 #===================== add data into employees table ===============#
# emp2 = create_employee(conn, 2, 'Kitt', 'Katt', 1900)
# emp3 = create_employee(conn, 1, 'Tom', 'Katt', 1900)
# emp4 = create_employee(conn, 4, 'Jerry', 'Mouse', 1800)
# emp5 = create_employee(conn, 5, 'Buggs', 'Bunny', 700)
# emp6 = create_employee(conn, 6, 'Tom', 'Ruffus', 1200)

 #===================== add data into guests  table ===============#
#-------  id, first_name, last_name, roomNo, checkIn, checkout --------------#
# guest1 = create_hotelGuests(conn,1,'Holmes', 'French', 10,'02-02-2021', '02-15-2021') 
# guest2 = create_hotelGuests(conn, 'Smith','Johnson', 4, '03/12/2020', '05-24-2020')
# guest3 = create_hotelGuests(conn, 'James','John',5, '12-1-2017', '01-02-2018')
# guest4 = create_hotelGuests(conn,'Mary','Patricia', 5,'12-1-2017', '01-02-2018' )
# guest5 = create_hotelGuests(conn,'Brown','Jones',7, '03-05-2018', '04-07-2018')
# guest6 = create_hotelGuests(conn, 'Richard','Charles',9, '07-05-2019', '08-07-2019')
# guest7 = create_hotelGuests(conn,'Linda','Rodriguez',8, '05-09-2022', '05-20-2022')
# guest7 = create_hotelGuests(conn,'Rohit','Purnam',6, '01-09-2022', '02-20-20122')
 
#========== add data into rooms  table  #roomId, price, num_of_beds================#
 
#room1 = create_rooms(conn,4, 150, 23)
# room2 = create_rooms(conn,5, 70, 2)
# room3 = create_rooms(conn,6, 87, 4)
# room4 = create_rooms(conn,7, 55, 1)
# room5 = create_rooms(conn,8, 100, 3)
# room6 = create_rooms(conn,9, 120, 2)

#==================== add to hotel table ================= #
#---( hotelId, hotel_name, city, state )---# 
#hotel1 = create_hotel(conn,'Transylvania : Transformania','Salt Lake City', 'UT', 2)

# c.execute("""DROP table guests """)

 

conn.close()