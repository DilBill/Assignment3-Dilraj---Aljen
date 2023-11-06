class Application:
    
    def showMainMenu():
        
        while True:
            
            selected = int(input(f"What Would You Like To Do?\nSelect Account: 1\nOpen Account: 2\nExit: 3"))
            
            if selected == 1:
                accNum = input("Enter Account Number: ")
            
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
        
        