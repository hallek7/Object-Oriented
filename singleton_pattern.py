
class Singleton:
    # check  if  Instance has been created or not
    __instance = None
    
    @staticmethod
    def getInstance(): # static method associated with hotel class to check if we need to create the instance
        if Singleton.__instance == None:
           Singleton()
        return Singleton.__instance

    def __init__(self): # this gets called to creat the hotel object 
       if Singleton.__instance != None: #  create hotel object only once 
          raise Exception (" object already exists ")
       else:
           Singleton.__instance = self
    
s = Singleton()
s = Singleton.getInstance()
print(s)
s = Singleton.getInstance()
print(s)
    # s3 = Hotel() will create new hotel obj, to prevent this throw an exception line 12 -