from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',18),fg='green')
L1.place(x=30,y=20)
####################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชี 100,000 บาท'
    messagebox.showwarning('เงินในบัญชี',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='เงินมีเท่าไร',command=Button2)
B2.pack(ipadx=20,ipady=20)
####################
def Button3():
    text = 'Python 101, Math'
    messagebox.showwarning('วิชาที่เรียนวันที่ 1-7 ก.ย.',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=180)
B3 = ttk.Button(FB1,text='สัปดาห์เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)

GUI.mainloop()

