from back_end_banking_system import Bank
from tkinter import *


class TkInterInterface:
    def __init__(self, name="Banking Management System", geometry="720x480"):
        self.__ROOT = Tk()
        self.__ROOT.title(name)
        self.__ROOT.geometry(geometry)

    def welcome_window(self, name="Banking Management System"):
        def create_account():
            frame = Frame(self.__ROOT)
            welcome_message = Label(frame, text=name + " Login Window")
            welcome_message.grid(column=2, row=0)
            frame.mainloop()

        def login():
            welcome_message = Label(self.__ROOT, text=name + " Login Window")
            welcome_message.grid(column=2, row=0)
            user_name_message = Label(self.__ROOT, text="Enter your username: ")
            user_name_message.grid(column=0, row=1)
            password_message = Label(self.__ROOT, text="Enter your password: ")
            password_message.grid(column=0, row=2)
            password = Entry(self.__ROOT)
            password.grid(column=1, row=3)
        test=LabelFrame(self.__ROOT, text="Lavel F")
        test.pack(expand="yes", fill="both")
        g=Label(test, text="op")
        g.place(x=0,y=5)
        mainloop()
        self.__ROOT.mainloop()

    def create_window(self, name="Welcome"):
        # self.__FRAME.pack()
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
    print(obj.welcome_window("ABhijit"))
