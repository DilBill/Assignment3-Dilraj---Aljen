import random
class Application:
    
    def showMainMenu():
        
        while True:
            
            selected = int(input(f"What Would You Like To Do?\nSelect Account: 1\nOpen Account: 2\nExit: 3\n"))
            
            if selected == 1:
                accNum = str(input("Enter Account Number: "))
                accFound = bank.searchAccount(accNum)
                if accFound == False:
                    print(f"No account found related to {accNum}")       
                else:
                    print("Account Found\nPlease Wait")
                    Application.showAccountMenu(bank,accFound)
            
            elif selected == 2:
                # call account class
                bank.openAccount()
            elif selected == 3:
                # leave main menu
                break
                
            elif selected != 1 or selected != 2 or selected != 3:
                print("Invaild Option Try Again")    
                
    def showAccountMenu(Bank,accIdx):
        
        while True:
            

            selected = int(input(f"What Would You Like To Do?\nCheck Balance: 1\nDeposit: 2\nWithdraw: 3\nExit: 4\n"))
            
            if selected == 1:
                # check account balance
                if accIdx == 1:
                    Bank.acc1.getCurrentBalance(accIdx,Bank)
                
                elif accIdx == 2:
                    Bank.acc2.getCurrentBalance(accIdx,Bank)
                    
                elif accIdx == 3:
                    Bank.acc3.getCurrentBalance(accIdx,Bank)
                
                elif accIdx >= 4:
                    Bank.newAcc.getCurrentBalance(accIdx,Bank)
                    
    
            elif selected == 2:
                # deposit money
                depositNum = int(input("Enter The Amount Of Money That You Would Like To Deposit: "))
                
                if accIdx == 1:
                    Bank.acc1._accountBalance = Bank.acc1.deposit(depositNum)
                    Bank.allAccounts.pop(accIdx - 1)
                    Bank.allAccounts.insert(accIdx - 1, Bank.acc1.toStr())
                    
                elif accIdx == 2:
                    Bank.acc2._accountBalance = Bank.acc2.deposit(depositNum)
                    Bank.allAccounts.pop(accIdx - 1)
                    Bank.allAccounts.insert(accIdx - 1, Bank.acc2.toStr())
                    
                elif accIdx == 3:
                    Bank.acc3._accountBalance = Bank.acc3.deposit(depositNum)
                    Bank.allAccounts.pop(accIdx - 1)
                    Bank.allAccounts.insert(accIdx - 1, Bank.acc3.toStr())
                    
                elif accIdx >= 4:
                    Bank.newAcc._accountBalance = Bank.newAcc.deposit(depositNum)
                    Bank.allAccounts.pop(accIdx - 1)
                    Bank.allAccounts.insert(accIdx - 1, Bank.newAcc.toStr())
                    
        
                else:
                    print("Invalid input Try Again ")
                        
            
            elif selected == 3:
            # withdraw money
                withdrawNum = input("Enter How Much Money You Would Like To Take Out:")
            elif selected == 4:
                # leave main menu
                break
                
            elif selected != 1 or selected != 2 or selected != 3 or selected != 4:
                print("Invaild Option Try Again")
            
    def run():
        Application.showMainMenu()
        

class Bank:
    
    def __init__(self, name):
        self._bankName = name
        self.allAccounts = []
        self.acc1 = Account(1000, "Aljen", 0.1, 75000)
        self.acc2 = Account(1010, "Raj", 0.1, 65000)
        self.acc3 = Account(1100, "Connor", 0.1, 70000)
        self.saving1 = savingAccount(5000)
        self.saving2 = savingAccount(4000)
        self.saving3 = savingAccount(4500)
        self.chequing1 = chequingAccount(2500)
        self.chequing2 = chequingAccount(1500)
        self.chequing3 = chequingAccount(2000)
        self.allAccounts.append(self.acc1.toStr())
        self.allAccounts.append(self.acc2.toStr())
        self.allAccounts.append(self.acc3.toStr())
        
    def openAccount(self):
        # open a new account
        accId = random.randint(1111,99999)
        name = input("Please Provide A Name For The Account: ")
        balance = int(input("How Much Do You want To Depsoit Into The Account?  \nPlease Enter A Numeric Value No characters or symbols: "))
        self.newAcc = Account(accId, name, 0.1, balance)
        print(self.newAcc.toStr())
        self.allAccounts.append(self.newAcc.toStr())
        
    def searchAccount(self, accNum):
        # search for an account in the bank
        idx = 0
        for a in self.allAccounts:
            acc = a
            commaIdx = acc.find(",")
            if accNum == acc[:commaIdx]:
                return idx + 1
            else:
                idx += 1
                
      
        return False
        
        
        
        
class Account:
    
    def __init__(self,accNum,holderName, intrest, balance):
        
        self._accountNumber = accNum
        self._accountHolderName = holderName
        self._intrestRate = intrest
        self._accountBalance = balance
        
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
        print(f"Your New Balance is ${self._accountBalance + depositNum}")
        return self._accountBalance + depositNum
    
    def withdraw(self,withdrawNum):
        return self.accountBalance - withdrawNum
    
    def getCurrentBalance(self,accIdx,Bank):
        
        print("Checking Balance...")
        balanceIdx = Bank.allAccounts[accIdx - 1].rfind(",")
        print(f"${Bank.allAccounts[accIdx - 1][balanceIdx + 1:]}")
    
    def toStr(self):
        return f"{self._accountNumber},{self._accountHolderName},{self._intrestRate},{self._accountBalance}"
    
class savingAccount:
    
    def __init__(self,minBalance):
        self._minimumBalance = minBalance
        
    def withdraw(self, withdrawNum):
        if Account.getCurrentBalance() - withdrawNum < self._minimumBalance:
            print("Sorry! You cannot withdraw that amount")
            
        else:
            Account.withdraw(withdrawNum)
            print("transication complete")
    
class chequingAccount:
    
    def __init__(self,overDraft):
        self._overDraftLimit = overDraft 
        
    def withdraw(self, withdrawNum):
        if (Account.getCurrentBalance() + self._overDraftLimit) - withdrawNum < 0:
            print("Sorry! You do not have enough money in your account to cover this transaction.")
        
        else:
            Account.withdraw(withdrawNum)
            print("Transaction Complete")
            

bank = Bank("RAJ'S BANK")
Application.run()