import time
print("Please enter your ATM card")
time.sleep(5)
pin = int(input("Enter your four digit ATM pin "))
balance = 1000
if pin == 1234:
    while True:
        print("1-Check Balance")
        print("2-Withdraw Money")
        print("3-Deposit Money")
        print("4-Exit")
        try:
            option = int(input("Choose Option Above: "))
        except:
            print("Please Enter Valid Option")
        if option == 1:
            print(f"Your Current Balance is{balance}")
        elif option == 2:
            withdrawmoney = int(input("Enter your withdraw amount:"))
            if balance>withdrawmoney:
               balance = balance - withdrawmoney
               print(f"{withdrawmoney} is debited from your account")
               print(f"Your current balance is {balance}")
            else:
                print("Insufficient Balance")
        
        elif option == 3:
            depositmoney = int(input("Enter the amount to be deposited:"))
            balance = balance + depositmoney
            print(f"{depositmoney} is credited to your account")
            print(f"Your current balance is {balance}")

        elif option == 4:
            print("Thank You for visiting our ATM machine...See you Again!")
            break


else:
    print("You entered wrong pin..Try Again")
