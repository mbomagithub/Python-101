from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('e-Document')
GUI.geometry('500x500')

L1 = Label(GUI,text='บันทึกข้อความ',font=('angsana new',22),fg='blue')
L1.pack()

L2 = Label(GUI,text='สำนัก/กอง',font=('angsana new',14),fg='black')
L2.place(x=30,y=50)
A1 = ttk.Combobox(value=["สำนักปลัด","กองคลัง","กองช่าง","กองสาธารณสุข","กองการศึกษา"])
A1.place(x=100,y=50)
    
FB1 = Frame(GUI)
FB1.place(x=300,y=50)
B1 = Button(FB1,text='ออกเลข',bg='green',fg='white')
B1.pack(ipadx=15)

###########################
L3 = Label(GUI,text='เลขที่',font=('angsana new',14),fg='black')
L3.place(x=30,y=80)
FA2 = Frame(GUI)
FA2.place(x=100,y=80)
A2 = ttk.Entry(FA2)
A2.pack(ipady=1)

L4 = Label(GUI,text='วันที่',font=('angsana new',14),fg='black')
L4.place(x=270,y=80)
FA3 = Frame(GUI)
FA3.place(x=300,y=80)
A3 = ttk.Entry(FA3)
A3.pack(ipady=1)

##########################
L5 = Label(GUI,text='ชั้นความเร็ว',font=('angsana new',14),fg='black')
L5.place(x=30,y=110)
A4 = ttk.Combobox(value=["ปกติ","ด่วน","ด่วนมาก","ด่วนที่สุด"])
A4.place(x=100,y=110)

L6 = Label(GUI,text='เรียน',font=('angsana new',14),fg='black')
L6.place(x=30,y=140)
FA5 = Frame(GUI)
FA5.place(x=100,y=140)
A5 = ttk.Entry(FA5)
A5.pack(ipadx=120,ipady=1)

L7 = Label(GUI,text='เรื่อง',font=('angsana new',14),fg='black')
L7.place(x=30,y=170)
FA6 = Frame(GUI)
FA6.place(x=100,y=170)
A6 = ttk.Entry(FA6)
A6.pack(ipadx=120,ipady=30)

############################
def Save():
    text = A1.get()
    print("หน่วยงาน : ",text)
    text1 = A2.get()
    print("เลขที่ : ",text1)
    text2 = A3.get()
    print("วันที่ : ",text2)
    text3 = A4.get()
    print("ชั้นความเร็ว : ",text3)
    text4 = A5.get()
    print("เรียน : ",text4)
    text5 = A6.get()
    print("เรื่อง : ",text5)     
    A1.delete(0,END)
    A2.delete(0,END)
    A3.delete(0,END)
    A4.delete(0,END)
    A5.delete(0,END)
    A6.delete(0,END)
    text = 'บันทึกสำเร็จ'
    messagebox.showinfo('SAVE',text)
    
FB2 = Frame(GUI)
FB2.place(x=100,y=280)
B2 = Button(FB2,text='บันทึกข้อมูล',bg='red',fg='white',command=Save)
B2.pack(ipadx=1)

FB3 = Frame(GUI)
FB3.place(x=200,y=280)
B3 = Button(FB3,text='แก้ไข',bg='yellow',fg='black')
B3.pack(ipadx=15)



GUI.mainloop()
