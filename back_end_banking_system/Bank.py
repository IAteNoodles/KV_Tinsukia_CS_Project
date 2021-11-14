import sys
import csv
import datetime
#from connection_mysql import MySQL
import pickle


class User:
    def __init__(self, customer_name: str, customer_address: str, customer_dob: str, customer_phone_number: str,
                 customer_email: str, account_type: str, first_deposit=0):
        """
        :param customer_name: Name of the user
        :param account_type: The type of account the user has selected
        :param first_deposit: The first deposit that is to be made on creating an account. Minimum deposit is set at Rs. 1000
        Inputs the data provided by the user which will then be used to create the account.
        """

        self.CUSTOMER_NAME = customer_name
        self.CUSTOMER_ADDRESS = customer_address
        self.CUSTOMER_DOB = customer_dob
        self.CUSTOMER_PHONE_NUMBER = customer_phone_number
        self.CUSTOMER_EMAIL = customer_email
        self.ACCOUNT_TYPE = account_type
        self.__IFSC__ = "000LIGN"
        account_number = str().__add__(self.__IFSC__)
        if account_type == 1:
            account_number = account_number.__add__("SAV")
        elif account_type == 2:
            account_number = account_number.__add__("CUR")
        else:
            account_number = account_number.__add__("COR")
        self.module_path = r"/home/groot/PycharmProjects/KV_Tinsukia_CS_Project/"
        count = int(open(self.module_path+r"back_end_banking_system/user_record.txt").read(4))
        account_number = account_number.__add__("0" * (4 - len(str(count)))).__add__(str(count))
        self.ACCOUNT_NUMBER = account_number
        self.ACCOUNT_BALANCE = first_deposit
        self.ACCOUNT_PASSBOOK_PATH = self.module_path+r"/Accounts/" + str(self.ACCOUNT_NUMBER) + "_info.dat"
        self.__TRANSACTIONS__ = open(self.module_path+r"/Accounts/" + str(self.ACCOUNT_NUMBER) + "._passbook.csv", "w",
                                     encoding="UTF8",
                                     newline="")
        self.__TRANSACTIONS_ROWS__ = ["DATE ",
                                      "PARTICULARS ",
                                      "CHEQUE NO ",
                                      "DEBIT ",
                                      "CREDIT ",
                                      "BALANCE "]
        open(r"../back_end_banking_system/user_record.txt", "w").write(str(count + 1))

    def create_account(self) -> bool:
        """
        :returns: True if account created else False.
        Looks for any errors in the credentials, and creates a new bank account.
        """
        with open(self.ACCOUNT_PASSBOOK_PATH, "wb") as input_details:
            input_data = [str("Account Number: " + self.ACCOUNT_NUMBER + "\n"),
                          str("Name: " + self.CUSTOMER_NAME + "\n"),
                          str("Address: " + self.CUSTOMER_ADDRESS + "\n"),
                          str("Date of Birth: " + str(self.CUSTOMER_DOB) + "\n"),
                          str("Phone: " + self.CUSTOMER_PHONE_NUMBER + "\n"),
                          str("Email: " + self.CUSTOMER_EMAIL + "\n"),
                          str("Account TYPE: " + self.ACCOUNT_TYPE + "\n"),
                          str("Current Balance: " + str(self.ACCOUNT_BALANCE) + "\n")]
            for data in input_data:
                pickle.dump(data, input_details)
            return True

    def link_passbook(self) -> None:
        """
        Creates a passbook which is linked with the user and updates it with the first transaction
        """
        update = {"DATE ": datetime.date.today(),
                  "PARTICULARS ": "CASH DEPOSIT SELF",
                  "CHEQUE NO ": "",
                  "DEBIT ": "",
                  "CREDIT ": self.ACCOUNT_BALANCE,
                  "BALANCE ": self.ACCOUNT_BALANCE}
        entry = csv.DictWriter(self.__TRANSACTIONS__, fieldnames=self.__TRANSACTIONS_ROWS__)
        entry.writeheader()
        entry.writerow(update)

    def deposit(self, balance: int) -> str:
        """
        :param balance: Money to be deposited
        :return: A confirmatory message
        Adds the amount to the current user balance
        """
        self.ACCOUNT_BALANCE += balance
        update = {"DATE ": datetime.date.today(),
                  "PARTICULARS ": "CASH DEPOSIT SELF",
                  "CHEQUE NO ": "",
                  "DEBIT ": "",
                  "CREDIT ": balance,
                  "BALANCE ": self.ACCOUNT_BALANCE}
        entry = csv.DictWriter(self.__TRANSACTIONS__, fieldnames=self.__TRANSACTIONS_ROWS__)
        entry.writerow(update)
        return str(balance) + " has been deposited into your account.\n Current Balance is " + str(self.ACCOUNT_BALANCE)


def accept_input() -> tuple:
    """
    :return: A tuple containing the user input (name, address, date of birth, phone number, email address, account type)
    Prompts the user to enter the details in order to create an account
    """
    customer_name = input("Enter your name: ")
    customer_address = input("Enter your address: ")
    customer_dob = input("Enter your date of birth (YYYY-MM-DD): ").split("-")
    customer_dob = datetime.date(int(customer_dob[0]),  # Year
                                 int(customer_dob[1]),  # Month
                                 int(customer_dob[2]))  # Date
    customer_phone_number = input("Enter your phone number: ")
    customer_email = input("Enter your email address: ")
    print("Account Types Available:")
    print("1)Savings\n2)Current\n3)Corporate")
    account_type = int(input("Enter your choice: "))
    if not 0 < account_type <= 3:  # Checks if the user has selected a valid account type
        sys.stderr.write("INVALID INPUT!!!")
        sys.stderr.flush()
        if not input("Press any key to retry and enter to end: ") is None:
            accept_input()  # Recursion
    account_type = "Savings" if account_type == 1 else "Current" if account_type == 2 else "Corporate"
    return customer_name, customer_address, customer_dob, customer_phone_number, customer_email, account_type  #
    # Returning the values in the form of a tuple


def prompt_user():
    name, address, dob, phone_number, email, acc_type = accept_input()  # Unpacking the tuple
    while True:  # Asks user for their first deposit
        first_dep = int(input("Please deposit the minimum balance (Rs. 1000):\n Deposit: "))
        if first_dep >= 1000:
            break
        print("Please deposit an amount >= 1000")
    user = BankConnection(name, address, dob, phone_number, email, acc_type, first_dep)
    user.create_account()
    user.link_passbook()
    return "Account created successfully!!!"


def retrieve_date(user_file):
    user_data: list = [str(), str(), str(), str(), int(), str(), str(), str()]
    count = 0
    try:
        while True:
            user_data[count] = (pickle.load(user_file)).strip()
            count += 1
    except EOFError:
        user_file.close()
    user_transaction_path = r"./Accounts/" + str(user_data[0]) + ".csv"
    user_data.append(user_transaction_path)
    return user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6], user_data[
        7]


def display_data(user_details: tuple):
    account_number, name, address, dob, phone_number, email, acc_type, transaction = user_details
    print(acc_type)
    print(account_number)
    print(name)
    print(address)
    print(phone_number)
    print(dob)


if __name__ == '__main__':
    #__CONNECTOR = MySQL.MySQLConnection("localhost", "python", "python", "bank")
    #__CONNECTOR.test()
    pass
