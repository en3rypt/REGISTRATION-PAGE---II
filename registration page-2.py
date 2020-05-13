from tkinter import *
from tkinter import messagebox
import mysql.connector as sql

mycon = sql.connect(host = 'localhost', user = 'root', passwd = 'root',database = 'test')
cur = mycon.cursor()


root = Tk()

def submit():
    name = t1.get()
    user_name = t2.get()
    email = t3.get()
    passwd = t4.get()
    cpasswd = t5.get()
    if name and user_name and email and passwd and cpasswd:
        cur.execute('select username,email from register')
        total = cur.fetchall()
        username = []
        exist_email = []
        for i in total:
            username.append(i[0])
            exist_email.append(i[1])

        if email in exist_email:
            messagebox.shoinfo('ALERT!','EMAIL ALREADY REGISTERED')
            e3.delete(0,END)
            
        else:
            if user_name in username:
                messagebox.showinfo('ALERT!','USERNAME ALREADY TAKEN')
                e2.delete(0,END)
            else:
                if passwd == cpasswd:
                    exe = f'insert into register values("{name}","{user_name}","{email}","{passwd}")'
                    cur.execute(exe)
                    mycon.commit()
                    messagebox.showinfo('SUCCESS!','REGISTRATION COMPLETED')
                    e1.delete(0,END)
                    e2.delete(0,END)
                    e3.delete(0,END)
                    e4.delete(0,END)
                    e5.delete(0,END)
                else:
                    messagebox.showinfo('ALERT!','PASSWORDS DO NOT MATCH')
            
    else:
        messagebox.showinfo('ALERT!','ALL FIELDS ARE MUST BE FILLED')
        


root.geometry('700x500')
root.title('REGISTRATION PAGE')
root.configure(bg = '#D3D3D3')
root.wm_iconbitmap('icon.ico')
root.resizable(0,0)


l0 = Label(root,text = 'REGISTRATION\n PAGE',font = ('normal',25,'bold'),bg = '#D3D3D3')
l0.place(x = 220 , y =60)

l1 = Label(root,text = 'NAME',font = ('arial',15,'normal'),bg = '#D3D3D3')
l1.place(x = 205 , y =160 )

l2 = Label(root, text = 'USER NAME',font = ('arial',15,'normal'),bg = '#D3D3D3')
l2.place(x =150 ,y =195 )

l3 = Label(root, text = 'EMAIL',font = ('arial',15,'normal'),bg = '#D3D3D3')
l3.place(x =205 ,y =230 )

l4 = Label(root, text = 'PASSWORD',font = ('arial',15,'normal'),bg = '#D3D3D3')
l4.place(x =150 ,y =265 )

l5 = Label(root, text = 'CONFIRM PASSWORD',font = ('arial',15,'normal'),bg = '#D3D3D3')
l5.place(x =55 ,y =300 )

# stringvar
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()

e1 = Entry(root, width = 20, font =('normal',15),bd = 3,textvariable = t1)
e1.place(x = 300, y =160)

e2 = Entry(root, width = 20, font =('normal',15),bd = 3,textvariable = t2)
e2.place(x = 300, y =195)

e3 = Entry(root, width = 20, font =('normal',15),bd = 3,textvariable = t3)
e3.place(x = 300, y =230)

e4 = Entry(root, width = 20, font =('normal',15),bd = 3,show = '*',textvariable = t4)
e4.place(x = 300, y =265)

e5 = Entry(root, width = 20, font =('normal',15),bd = 3,show = '*',textvariable = t5)
e5.place(x = 300, y =300)

b1 = Button(root,text = 'SUBMIT',font =('normal',15),bd = 3,command = submit)
b1.place(x = 330 , y = 350)

root.mainloop()
