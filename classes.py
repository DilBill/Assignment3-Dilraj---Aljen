import random
class Application:
    
    def showMainMenu():
        
        while True:
            
            selected = int(input(f"What Would You Like To Do?\nSelect Account: 1\nOpen Account: 2\nExit: 3"))
            
            if selected == 1:
                accNum = input("Enter Account Number: ")
                if Bank.searchAccount(accNum):
                    print("account found \nPlease wait")
            
            elif selected == 2:
                # call account class
                account = 0
            
            elif selected == 3:
                # leave main menu
                mainMenu = 0
                
            elif selected != 1 or selected != 2 or selected != 3:
                print("Invaild Option Try Again")    
                
    def showAccountMenu():
        
        while True:
            
            selected = int(input(f"What Would You Like To Do?\nCheck Balance: 1\nDeposit: 2\nWithdraw: 3\nExit: 4"))
            
            if selected == 1:
                # check account balance
                balance = 0
            
            elif selected == 2:
                # deposit money
                depositamount = 0
            
            elif selected == 3:
            # withdraw money
                withdrawamount = 0
            elif selected == 4:
                # leave main menu
                mainMenu = 0
                
            elif selected != 1 or selected != 2 or selected != 3 or selected != 4:
                print("Invaild Option Try Again")
            
    def run():
        Application.showMainMenu()
        

class Bank:
    
    def __init__(self, name):
        self._bankName = name
        
        accounts = []
        acc1 = Account(1000, "Jim", 0.1, 5000)
        accounts.append(acc1)
        acc2 = Account(1010, "carl", 0.2, 65000)
        accounts.append(acc2)
        acc3 = Account(1019, "tony", 0.25, 78550)
        accounts.append(acc3)
        

    def openAccount(self):
        # open a new account
        accNum = random.randint(1000,100000)
        name = input("Please provide the name for the account")
        balance = 0
        intrest = 0.1
        newAcc = Account(accNum, name, intrest, balance)
    
        
        
    def searchAccount(self):
        # search for an account in the bank
        
        foundAcc = 0
        
        
class Account:
    
    def __init__(self,accNum, holderName, intrest, balance):
        
        self._accountNumber = accNum
        self._accountHolderName = holderName
        self._intrestRate = intrest
        self.accountBalance = balance
        
    def getAccountNum(self):
        return self._accountNumber
    
    def getAccountHolderName(self):
        return self._accountHolderName
    
    def setAccountHolderName(self,newName):
        self._accountHolderName = newName
    
    def getIntrestRate(self):
        return self._intrestRate
    
    def setInterstRate(self,newIntrest):
        self._intrestRate = newIntrest
        
    def deposit(self, depositNum):
        return self.accountBalance + depositNum
    
    def withdraw(self,withdrawNum):
        return self.accountBalance - withdrawNum
    
class savingAccount:
    
    def __init__(self,minBalance):
        self._minimumBalance = minBalance
        
    def withdraw(self, withdrawNum):
        return self.minimumBalance - withdrawNum
    
class chequingAccount:
    
    def __init__(self,overDraft):
        self._overDraftLimit = overDraft 
        
    def withdraw(self, withdrawNum):
        return self.overDraftLimit - withdrawNum
        
    