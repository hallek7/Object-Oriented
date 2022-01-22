class CheckingAccount:
    def __init__(self):
        self.__balance = 0
         
    def credit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.__balance += amount
         
        
    def withdraw(self):
        amount = float(input("Enter amount you want to withdraw: "))
        if self.__balance >= amount: #if amount withdrawn is >= currenet balance 
           self.__balance -= amount # current balance will be less than amt withdrawn
            
        else: 
             print("\n Insufficient balance.")

    def balance_remaing(self):
        print(" Net Available Balance=",self.__balance)
          
def main():    # creating an object of class
     ck = CheckingAccount()
     name = input("Enter your name : ")
     __accNumber = input("Enter your account number : ")
     
     ck.credit()
     ck.withdraw()
    
      
     print("\n Account Name : ", name)
     print(" Account Number is : ", __accNumber)
     ck.balance_remaing()
main()