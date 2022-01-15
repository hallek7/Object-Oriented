class Teams:
    def __init__(self, members):
      self.__myTeam = members

    def __len__(self):
      return len(self.__myTeam)
  # 1) Add the __contains__ protocol and show whether or not  'Tim' and 'Sam' are part of our team. 

    def __contains__(self, member):
      return member in self.__myTeam
 # 2) Add the __iter__ protocol and show how you can print each member of the classmates object.

    def __iter__(self):
      return iter(self.__myTeam)
  
 # 3) Determine if the class classmates implements the __len__ method.

def main():
   classmates = Teams(['John', 'Steve', 'Tim'])
   print ('Tim' in classmates)
   print ('Sam' in classmates)
   print (len(classmates))
   iterate = iter(classmates)
   for member in iterate: 
       print (member,end= " , ")
   
main()

 