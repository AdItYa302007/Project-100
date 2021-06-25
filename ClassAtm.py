class Atm(object):
    def __init__(self,cardnumber,pin,expiry):
        self.cardnumber=cardnumber
        self.pin=pin
        self.expiry=expiry

    def check_balance(self):
        print("Your Balance Is 100000")

    def withdrawl(self,amount):
        new_amount = 100000 - amount
        print("You Have Succesfully Withdrawn Amount Of "+str(amount) +". Your Remaining Balance Is "+ str(new_amount))


def main():
    Card_number=input("Enter Your Card Number- ")
    pin_number=input("Enter Your Pin Number- ")
    expiry_number=input("Enter Your Card Expiry Date-")
    new_user=Atm(Card_number,pin_number,expiry_number)

    print("Select Your Service ")
    print("1.Balance Enquriy   2.Withdraw Money")
    option = int(input("Enter Service Number- "))

    if (option == 1):
        new_user.check_balance()
    elif (option == 2):
        amount = int(input("Enter The Amount- "))
        new_user.withdrawl(amount)
    else:
        print("Enter A Valid Number")


if __name__ == "__main__":
    main()