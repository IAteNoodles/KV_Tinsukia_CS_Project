from tkinter import *
import sys
sys.path.append('/home/groot/KV_Tinsukia_CS_Project/back_end_banking_system/')
import Bank

class GUI:
    def __init__(self, name="Name of the bank", geometry="720x480"):
        self.__ROOT = Tk()
        self.__ROOT.title(name)
        self.__ROOT.geometry(geometry)

    def start_up(self):
        userFrame = LabelFrame(self.__ROOT,text="User", fg="Green")
        userFrame.pack(expand = True, fill = 'both')
        def login_user():
            
            login_window = Toplevel(self.__ROOT)
            login_window.title("Account Login Window")
            login_window.geometry("640x400")
            
            Label(login_window, text="Unique ID: ").pack(anchor = CENTER)
            unique_id = Entry(login_window)
            unique_id.pack(anchor = CENTER)
            unique_id = unique_id.get()
            
            Label(login_window, text="Password: ").pack(anchor = CENTER)
            password = Entry(login_window)
            password.pack(anchor = CENTER)
            password = password.get()
            
            def check_credentials():
                pass
            Button(login_window, text="Confirm", command = check_credentials).pack(anchor = CENTER)
            
        Button(userFrame, text="Login", command = login_user).pack(anchor = CENTER)
        def create_account():
            pass
        Button(userFrame,text="Create an new account", command = create_account).pack(anchor = CENTER)
        adminFrame = LabelFrame(self.__ROOT,text="Admin", fg="Blue")
        adminFrame.pack(expand = True, fill = 'both')
        helpFrame = LabelFrame(self.__ROOT, text="Help", fg="Red")
        helpFrame.pack(expand = True, fill = 'both')
        self.__ROOT.mainloop()
GUI().start_up()
