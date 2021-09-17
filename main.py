import sys


class Bank:
    def __init__(self, customer_name, account_type):
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


def accept_input():
    customer_name = input("Enter your name: ")
    print("Account Types Available:")
    print("1)Savings\n2)Current\n3)Corporate")
    account_type = int(input("Enter your choice: "))
    if not 0 < account_type <= 3:
        sys.stderr.write("INVALID INPUT!!!")
        sys.stderr.flush()
        if not input("Press any key to retry and enter to end: ") is None:
            accept_input()
    account_type = "Savings" if account_type == 1 else "Current" if account_type == 2 else "Corporate"
    a = Bank(customer_name, account_type)
    print(a.__dict__)


if __name__ == '__main__':
    accept_input()
