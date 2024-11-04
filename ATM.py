print("Welcome to so bank")
pin=int(input("Enter your 4 digit pin: "))
amount=12000
if(pin==1234):
    print("1-Withdraw")
    print("2-Balance Enquiry")
    print("3-Fast Cash")
    c=int(input("choose the transaction"))
    if(c==1):
        w=int(input("enter the withdraw amount"))
        if(w<=amount):
            print("the withdraw amount is ",w)
            amount -= w
            print("The remaining amount is ",amount)
        else:
            print("Invalid Cash")
    elif(c==2):
        print("the available amount in the account is",amount)
    elif(c==3):
        print("1->5000/-")
        print("2->10000/-")
        print("3->15000/-")
        fastcash=int(input("Enter the fast cash amount: "))
        if(fastcash==1 and 5000<amount):
            print("withdrawing 5000")
        elif(fastcash==2 and 10000<amount):
            print("withdraw 10000")
        else:
            print("invalid cash option")
else:
    print("Enter the right pin")