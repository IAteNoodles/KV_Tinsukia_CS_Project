import sys
import csv
import datetime
import os


class Bank:
    def __init__(self, customer_name: str, customer_address: str, customer_dob: str, customer_phone_number: str,
                 customer_email: str, account_type: str, first_deposit=0):
        """
        Inputs the data provided by the user which will then be used to create the account.
        @param customer_name: Name of the user
        @param account_type: The type of account the user has selected
        @param first_deposit: The first deposit that is to be made on creating an account.
        Minimum deposit is set at Rs. 1000
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
        count = int(open("user_record.txt").read(4))
        account_number = account_number.__add__("0"*(4-len(str(count)))).__add__(str(count))
        self.ACCOUNT_NUMBER = account_number
        self.ACCOUNT_BALANCE = first_deposit
        self.ACCOUNT_PASSBOOK_PATH = r"./Accounts/" + str(self.ACCOUNT_NUMBER) + "_info.txt"
        self.__TRANSACTIONS__ = open(r"./Accounts/" + str(self.ACCOUNT_NUMBER) + "._passbook.csv", "w", encoding="UTF8",
                                     newline="")
        self.__TRANSACTIONS_ROWS__ = ["DATE ",
                                      "PARTICULARS ",
                                      "CHEQUE NO ",
                                      "DEBIT ",
                                      "CREDIT ",
                                      "BALANCE "]
        open("user_record.txt", "w").write(str(count+1))

    def create_account(self) -> None:
        """
        Creates a new bank account and saves the information in a .txt file
        """
        with open(self.ACCOUNT_PASSBOOK_PATH, "w") as input_details:
            input_details.writelines([str("Account Number: " + self.ACCOUNT_NUMBER + "\n"),
                                      str("Name: " + self.CUSTOMER_NAME + "\n"),
                                      str("Address: " + self.CUSTOMER_ADDRESS + "\n"),
                                      str("Date of Birth: " + str(self.CUSTOMER_DOB) + "\n"),
                                      str("Phone: " + self.CUSTOMER_PHONE_NUMBER + "\n"),
                                      str("Email: " + self.CUSTOMER_EMAIL + "\n"),
                                      str("Account TYPE: " + self.ACCOUNT_TYPE + "\n"),
                                      str("Current Balance: " + str(self.ACCOUNT_BALANCE) + "\n")])

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
        Adds the amount to the current user balance
        @param balance: Money to be deposited
        @return: A confirmatory message
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
    Prompts the user to enter the details in order to create an account
    @return: A tuple containing the user input (name, address, date of birth, phone number, email address, account type)
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
    user = Bank(name, address, dob, phone_number, email, acc_type, first_dep)
    user.create_account()
    user.link_passbook()
    return "Account created successfully!!!"


def retrieve_date(user_file):
    user_data: list = user_file.readlines()
    user_account_number = user_data[0]
    user_name = user_data[1]
    user_address = user_data[2]
    user_dob = user_data[3]
    user_phone_number = user_data[4]
    user_email_address = user_data[5]
    user_account_type = user_data[6]
    user_transaction_path = r"./Accounts/"+str(user_account_number) + ".csv"
    return user_account_number, user_name, user_address, user_dob, user_phone_number, user_email_address, user_account_type, user_transaction_path


if __name__ == '__main__':
    print("\t\t\tWelcome")
    files = list(files for files in os.listdir("./Accounts"))
    account_list = list()
    for file in files:
        if file.__contains__("_info.txt"):
            account_list.append(str(int(file[10:14])+1).__add__(")"+file))
    account_list.reverse()
    for account in account_list:
        print(account.strip("_info.txt"))
    choice = int(
        input("Enter the Sl.No of the account that you want to log in.\n To create a new account, enter 0\nEnter "
              "your choice: "))
    if choice == 0:
        prompt_user()
    else:
        if choice >= len(account_list):
            index = account_list[choice - 1].find(")")
            path = r"./Accounts/" + account_list[choice - 1][index + 1::]
            account_number, name, address, dob, phone_number, email, acc_type, transaction = retrieve_date(open(path))
