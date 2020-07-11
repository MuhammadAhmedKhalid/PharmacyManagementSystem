from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter.ttk import Combobox
from abc import abstractmethod

# username = 'Muhammad'
# password= 'master111'

window = Tk()
LOGINTEXT = StringVar()
USERNAME = StringVar()
PASSWORD = StringVar()


class ActionHandler:
    login_count = 0

    @staticmethod
    def login_button_command():
        DataBaseHandler.create_user()
        is_success = DataBaseHandler.query_user()
        if (is_success):
            View.option_view(window)
        else:
            if ActionHandler.login_count == 3:
                window.destroy()
            else:
                ActionHandler.login_count = ActionHandler.login_count + 1
                LOGINTEXT.set("Note: Incorrect Username or Password, Please try again...")
    @staticmethod
    def medicine_button_command():
        View.medicine_window()
    @staticmethod
    def patient_button_command():
        View.add_patient_window()
    @staticmethod
    def buy_medicine_button_command():
        View.buy_medicine_window()
    @staticmethod
    def doctor_button_command():
        View.doctor_window()
    @staticmethod
    def consult_doctor_button_command():
        View.consult_doctor_window()
    @staticmethod
    def exit_button_command():
        exit()
    @staticmethod
    def add_company_button_command():
        View.add_company_window()
    @staticmethod
    def show_medicine_button_command():
        View.show_medicine_window()
    @staticmethod
    def save_company_button_command():
        View.save_company_window()
class DataBaseHandler:
    global con, cursor
    @staticmethod
    def create_user():
        con = sqlite3.connect("Pharmacy.db")
        cursor = con.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS 'USERS' (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
        cursor.execute("SELECT * FROM 'USERS' ORDER BY 'id' DESC LIMIT 1")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO 'USERS' ('username','password') VALUES('Muhammad','master111')")
        con.commit()

    @staticmethod
    def query_user():
        con = sqlite3.connect("Pharmacy.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM USERS WHERE username = ? AND password = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is None:
            return False
        else:
            return True

class Pharmacy:
    def __init__(self,doctors,medicines,patients):
        self.__doctors=doctors
        self.__medicines=medicines
        self.__patients=patients
    def getDoctors(self):
        return self.__doctors
    def getMedicines(self):
        return self.__medicines
    def getPatients(self):
        return self.__patients
    def setDoctor(self, doctor):
        self.__doctors=doctor
    def setMedicine(self,medicine):
        self.__medicines=medicine
    def setPatient(self,patient):
        self.__patients=patient

class Company:
    def __init__(self,name,description):
        self.__name=name
        self.__description=description
    def getName(self):
        return self.__name
    def getDescription(self):
        return self.__description
    def setName(self,name):
        self.__name=name
    def setDescription(self,description):
        self.__description=description

class Medicicnes:
    def __init__(self,company,name,type,amount,price):
        self.__company=company
        self.__name=name
        self.__type=type
        self.__amount=amount
        self.__price=price

class Patients:
    def __init__(self,name,gender,age,phoneNum,doctorConsulted,CNIC):
        self.name=name
        self.gender=gender
        self.age=age
        self.phoneNum=phoneNum
        self.doctorConsulted=doctorConsulted
        self.CNIC=CNIC

class Doctor:
    def __init__(self,name,age,gender,phoneNum,CNIC):
        self.name=name
        self.age=age
        self.gender=gender
        self.CNIC=CNIC
        self.phoneNum=phoneNum
    #@abstractmethod
    #def abc:
        #pass
class Cardiologist(Doctor):
    def __init__(self,name,age,gender,phoneNum,CNIC):
        super().__init__(name,age,gender,phoneNum,CNIC)

class Surgeon(Doctor):
    def __init__(self, name, age, gender, phoneNum, CNIC):
        super().__init__(name, age, gender, phoneNum, CNIC)


class View:
    @staticmethod
    def login_View(window):
        View.set_window(window)
        Label(window, text="\nInventory Management of Bin Hashim Pharmacy", font=("Basic Retro", 35),bg='Light Gray').pack()
        MainFrame = Frame(window).pack()
        HeadFrame = Frame(MainFrame).pack()
        Label(HeadFrame, text="\nLogin Screen\n", font=("Basic Retro", 20), bg='Light Gray').pack()
        image = Image.open("pic.png").convert("RGB")
        image = image.resize((200,200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        lbl = Label(HeadFrame, image=img,bg="Light Gray")
        lbl.image = img
        lbl.pack()
        Label(HeadFrame, text="\nUsername", font=("Basic Retro", 16), bg='Light Gray').pack()
        Entry(HeadFrame, bd=3, textvariable=USERNAME).pack()
        Label(HeadFrame, text="\nPassword", font=("Basic Retro", 16), bg='Light Gray').pack()
        Entry(HeadFrame, bd=3, show="*", textvariable=PASSWORD).pack()
        Label(HeadFrame, text="\n", bg='Light Gray').pack()
        Button(HeadFrame, text="Login", command=ActionHandler.login_button_command, fg='Gray', bg='Black',font=("Bold"), width=13).pack()
        Label(HeadFrame, textvariable=LOGINTEXT, font=("Basic Retro", 10), bg='Light Gray', fg='Red').pack()
    @staticmethod
    def option_view(window):
        window.destroy()
        window = Tk()
        Label(window, text="\nInventory Management of Bin Hashim Pharmacy", font=("Basic Retro", 35),bg='Light Gray').pack()
        View.set_window(window)
        Label(window, text="\n", bg='Light Gray').pack()
        Button(window,text='Add Medicine',command=ActionHandler.medicine_button_command,bd=3,fg='Black',bg='Gray',font=("Bold"),width=20,height=2).pack()
        Label(window,text="\n",bg='Light Gray').pack()
        Button(window,text='Add Patient',command=ActionHandler.patient_button_command,bd=3,fg='Black',bg='Gray',font=("Bold"),width=20,height=2).pack()
        Label(window,text="\n",bg='Light Gray').pack()
        Button(window,text='Buy Medicine',command=ActionHandler.buy_medicine_button_command,bd=3,fg='Black',bg='Gray',font=("Bold"),width=20,height=2).pack()
        Label(window,text="\n",bg='Light Gray').pack()
        Button(window,text='Doctor',command=ActionHandler.doctor_button_command,bd=3,fg='Black',bg='Gray',font=("Bold"),width=20,height=2).pack()
        Label(window,text="\n",bg='Light Gray').pack()
        Button(window,text='Consult Doctor',command=ActionHandler.consult_doctor_button_command,bd=3,fg='Black',bg='Gray',font=("Bold"),width=20,height=2).pack()
        Label(window,text="\n",bg='Light Gray').pack()
        Button(window,text='Exit',command=ActionHandler.exit_button_command,bd=3,fg='Black',bg='Gray',font=("Bold"),width=20,height=2).pack()
        window.mainloop()
    @staticmethod
    def set_window(setup):
        setup.title("Inventory Management of Bin Hashim Pharmacy")
        width = setup.winfo_screenwidth()
        height = setup.winfo_screenheight()
        setup.geometry(f'{width}x{height}')
        setup.config(bg='Light Gray')
    @staticmethod
    def medicine_window():
        window = Toplevel()
        Label(window, text="Medicine Detail",font=("Basic Retro",35),bg='Light Gray').pack()
        View.set_window(window)
        Label(window,text="\nName",font=("Basic Retro", 16),bg='Light Gray').pack()
        Entry(window,bd=3).pack()
        Label(window, text="\nType",font=("Basic Retro", 16),bg='Light Gray').pack()
        combo=Combobox(window)
        combo['values']=('Choose..','Liquid','Tablet','Capsule','Drops','Injection', 'Text')
        combo.current(0)
        combo.pack()
        Label(window, text="\nAmount",font=("Basic Retro", 16),bg='Light Gray').pack()
        Entry(window, bd=3).pack()
        Label(window, text="\nPrice",font=("Basic Retro", 16),bg='Light Gray').pack()
        Entry(window, bd=3).pack()
        Label(window, text="\nCompany",font=("Basic Retro", 16),bg='Light Gray').pack()
        combo = Combobox(window)
        combo['values'] = ('Choose..','1','2','3','Text')
        combo.current(0)
        combo.pack()
        Label(window,text="\n", bg='Light Gray').pack()
        Button(window,text='Add Company',command=ActionHandler.add_company_button_command,bd=3,fg='Black',bg='Gray',font=("Bold"),width=20,height=1).pack()
        Label(window,text="\n", bg='Light Gray').pack()
        Button(window,text='Show Medicine',command=ActionHandler.show_medicine_button_command,bd=3,fg='Black',bg='Gray',font=("Bold"),width=20,height=1).pack()
        Label(window, text="\n", bg='Light Gray').pack()
        Button(window,text='Save',command=ActionHandler.save_button_command,bd=3,fg='Black',bg='Gray',font=("Bold"),width=20,height=1).pack()
        window.mainloop()
    @staticmethod
    def add_patient_window():
        window = Toplevel()
        Label(window, text="\nAdd Patient",font=("Basic Retro",35),bg='Light Gray').pack()
        View.set_window(window)
        window.mainloop()
    @staticmethod
    def buy_medicine_window():
        window = Toplevel()
        Label(window, text="\nBuy Medicine",font=("Basic Retro",35),bg='Light Gray').pack()
        View.set_window(window)
        window.mainloop()
    @staticmethod
    def doctor_window():
        window = Toplevel()
        Label(window, text="\nDoctors Details", font=("Basic Retro", 35), bg='Light Gray').pack()
        View.set_window(window)
        window.mainloop()
    @staticmethod
    def consult_doctor_window():
        window = Toplevel()
        Label(window, text="\nConsult Doctor", font=("Basic Retro", 35), bg='Light Gray').pack()
        View.set_window(window)
        window.mainloop()
    @staticmethod
    def add_company_window():
        window = Toplevel()
        Label(window, text="\nAdd Company", font=("Basic Retro", 35), bg='Light Gray').pack()
        View.set_window(window)
        window.mainloop()
    @staticmethod
    def show_medicine_window():
        window = Toplevel()
        Label(window, text="\nShow Medicine", font=("Basic Retro", 35), bg='Light Gray').pack()
        View.set_window(window)
        window.mainloop()
    @staticmethod
    def save_company_window():
        window = Toplevel()
        Label(window, text="\nSave Company Window", font=("Basic Retro", 35), bg='Light Gray').pack()
        View.set_window(window)
        window.mainloop()
if __name__ == '__main__':
    View.login_View(window)
    window.mainloop()