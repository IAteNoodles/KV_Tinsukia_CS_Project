from tkinter import *


class TkInterInterface:
    def __init__(self, name="Banking Management System", geometry="720x480"):
        self.__ROOT = Tk()
        self.__FRAME = Frame(self.__ROOT)
        self.__ROOT.title(name)
        self.__ROOT.geometry(geometry)

    def login_window(self, name):
        welcome_message = Label(self.__ROOT, text="Welcome " + name + "!!!")
        welcome_message.grid(column=2, row=0)
        password_message = Label(self.__ROOT, text="Enter your password: ")
        password_message.grid(column=0, row=1)
        password = Entry(self.__ROOT)
        password.grid(column=1, row=1)

        def clicked():
            password_message.configure(text=password.get())


        button = Button(self.__ROOT, text="Login", fg="red", command=clicked)
        button.grid(column=2, row=1)
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
    print(obj.login_window("ABhijit"))
