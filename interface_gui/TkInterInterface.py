from tkinter import *
from back_end_banking_system import Bank


class TkInterInterface:
    def __init__(self, name="Banking Management System", geometry="720x480"):
        self.__ROOT = Tk()
        self.__ROOT.title(name)
        self.__ROOT.geometry(geometry)

    def welcome_window(self, name="Banking Management System"):
        def signup():
            welcome_frame.destroy()
            signup_frame = Frame(self.__ROOT)
            welcome_message = Label(signup_frame, text=name + " Signup Window")
            welcome_message.grid(column=1, row=0)
            unique_id_message = Label(signup_frame, text="Unique ID: ")
            unique_id_message.grid(column=0, row=1)
            unique_id = Entry(signup_frame)
            unique_id.grid(column=1, row=1)
            unique_id = unique_id.get()
            signup_frame.grid(column=0, row=0)

            def back():
                signup_frame.destroy()
                self.welcome_window()

            back = Button(signup_frame, text="Back to the previous window", fg="red", command=back)
            back.grid(column=3, row=4)

            def get_details():
                # Checks if there is an account with the unique id in the database
                # Checks if the name entered matches with the name in the database
                # If the above conditions are satisfied, then it proceeds to the next stage
                get_details_frame = Frame(self.__ROOT)
                get_details_frame.grid(column=0, row=0)
                # Imports Name, Address, Date of Birth, Phone, Email from the database
                _name, address, dob, phone_number, email = "User", "Address", "1111/11/11", "1234567890", "@gmail.com"
                signup_frame.destroy()

                def create_account():
                    get_details_frame.destroy()
                    creation_frame = Frame(self.__ROOT)
                    creation_frame.grid(column=0, row=0)
                    Label(creation_frame, text="Unique Id:" + unique_id).grid(column=0, row=0)
                    account_type_options = StringVar(self.__ROOT)
                    account_choices = {"Savings", "Current", "Corporate"}
                    account_type_options.set("Savings")
                    account_type_dropdown_menu = OptionMenu(creation_frame, account_type_options, *account_choices)
                    Label(creation_frame, text="Name: {0}\n"
                                               "Address: {1}\n"
                                               "Date of birth: {2}\n"
                                               "Phone number: {3}\n"
                                               "Email: {4}".format(_name,
                                                                   address,
                                                                   dob,
                                                                   phone_number,
                                                                   email)).grid(column=0, row=1)
                    Label(creation_frame, text="Account Type: ").grid(column=0, row=2)
                    account_type_dropdown_menu.grid(column=1, row=2)

                    def change_dropdown(*args):
                        return account_type_options.get()

                    account_type = account_type_options.trace("w", change_dropdown)
                    bank = Bank.BankConnection(_name, address, dob, phone_number, email, account_type)

                confirm_button = Button(get_details_frame, text="Confirm Details", command=create_account)
                confirm_button.grid(column=3, row=3)
                get_details_frame.mainloop()

            next_button = Button(signup_frame, text="Next >>>", command=get_details)
            next_button.grid(column=3, row=3)

        def login():
            welcome_frame.destroy()
            login_frame = Frame(self.__ROOT)
            welcome_message = Label(login_frame, text=name + " Login Window")
            welcome_message.grid(column=1, row=0)
            user_name_message = Label(login_frame, text="Name: ")
            user_name_message.grid(column=0, row=1)
            user_name = Entry(login_frame)
            user_name.grid(column=1, row=1)
            password_message = Label(login_frame, text="Unique ID: ")
            password_message.grid(column=0, row=2)
            password = Entry(login_frame)
            password.grid(column=1, row=2)
            login_frame.grid(column=0, row=0)

            def back():
                login_frame.destroy()
                self.welcome_window()

            back = Button(login_frame, text="Back to the previous window", fg="red", command=back)
            back.grid(column=3, row=4)

            def check(user: Entry, passwd: Entry) -> str:
                """
                :param user: Name of the user
                :param passwd: Password of the user
                :return:
                Gets the value from the user and runs a scan withing the database to find for an existing account. If
                the credentials provided match then logs in the user, else returns a message.
                """

            confirm_button = Button(login_frame, text="Confirm", command=check(user_name, password))
            confirm_button.grid(column=3, row=3)

        welcome_frame = Frame(self.__ROOT)
        welcome_frame.grid(column=0, row=0)
        login_button = Button(welcome_frame, text="Login", fg="blue", command=login)
        signup_button = Button(welcome_frame, text="New? Create an account!!!", fg="green", command=signup)
        login_button.grid(column=0, row=1)
        signup_button.grid(column=0, row=2)
        self.__ROOT.mainloop()

    def create_window(self, name="Welcome"):
        label = Label(self.__ROOT, text=name)
        label.grid()
        text = Entry(self.__ROOT, width=10)
        text.grid(column=1, row=0)

        def click():
            res = "Yo" + text.get()
            label.configure(text=res)

        button = Button(self.__ROOT, text="OP", fg="red", command=click)
        button.grid(column=2, row=0)
        self.__ROOT.mainloop()


if __name__ == "__main__":
    obj = TkInterInterface()
    print(obj.welcome_window("Bank of Sissami"))
