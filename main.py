import sys


class Bank:
    def __init__(self, customer_name: str, account_type: str):
        self.CUSTOMER_NAME = customer_name
        self.ACCOUNT_TYPE = account_type
        self.__IFSC__ = "000LIGN"
        account_number = str().__add__(self.__IFSC__)
        if account_type == 1:
            account_number = account_number.__add__("SAV")
        elif account_type == 2:
            account_number = account_number.__add__("CUR")
        else:
            account_number = account_number.__add__("COR")
        self.ACCOUNT_NUMBER = account_number


def accept_input() -> tuple:
    customer_name = input("Enter your name: ")
    customer_address = input("Enter your")
    print("Account Types Available:")
    print("1)Savings\n2)Current\n3)Corporate")
    account_type = int(input("Enter your choice: "))
    if not 0 < account_type <= 3:
        sys.stderr.write("INVALID INPUT!!!")
        sys.stderr.flush()
        if not input("Press any key to retry and enter to end: ") is None:
            accept_input()
    account_type = "Savings" if account_type == 1 else "Current" if account_type == 2 else "Corporate"
    return customer_name, account_type  # Returning the values in the form of a tuple


if __name__ == '__main__':
    print("\t\t\tWELCOME", end=" ")
    try:
        file = open(r"\.bank_details.txt")
    except FileNotFoundError:  # If the program finds no existing file in the working directory and prompts the user.
        with sys.stderr as print_error:
            print_error.write("\nYou currently have no existing account.")
            print_error.flush()
        print("Do you want to create a bank account?")
        user_choice = int(input("Enter 1 for yes and any number to end the program: "))
        if user_choice == 1:
            acc_type, name = accept_input()  # Unpacking the tuple
        else:
            print("Have a great day!!!")
