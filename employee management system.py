#!/usr/bin/env python
# coding: utf-8

# In[4]:


import mysql.connector
conn=mysql.connector.connect(user='root',password='Ajit@0077',host='localhost',db='project')
mycur=conn.cursor()
mycur.execute('Create table emp1(name varchar(40),mobno varchar(40),dept varchar(20),salary varchar(20))')
conn.close()


# In[1]:


import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

win=Tk()
win.title('Employee Management System')
win.minsize(width=1500,height=700)
win.configure(bg='#F0FFFF')

def emp(name,dept,mobno,salary):
    import mysql.connector
    conn=mysql.connector.connect(user='root',password='Ajit@0077',host='localhost',db='project')
    mycur=conn.cursor()
    mycur.execute('select exists(select * from emp1 where name="%s")'%name)
    for i in mycur:
        exists=i[0]
    try:
        if exists!=1: 
            mycur.execute('Insert into emp1 values("%s","%s","%s","%s")'%(name,mobno,dept,salary))
            conn.commit()
            s_lable.config(text='Employee Added Succesfully!!')
        else:
            mycur.execute('update emp1 set mobno="%s",dept="%s",salary="%s" where name="%s"'%(mobno,dept,salary,name))
            conn.commit()
            s_lable.config(text='Employee updated Succesfully!!')
    except:
        conn.rollback()
    conn.close()
    
def disp():
    name=v1.get()
    dept=v2.get()
    mobno=v3.get()
    salary=v4.get()
    if name=='' or mobno=='' or dept=='' or salary=='':
        messagebox.showinfo('Info','All feilds are complusary')
    else:
        emp(name,dept,mobno,salary)
    
def clear():
    v1.set('')
    v3.set('')
    v4.set('')
    s_lable.config(text='')    

def set_values(name):
    import mysql.connector
    conn=mysql.connector.connect(user='root',password='Ajit@0077',host='localhost',db='project')
    mycur=conn.cursor()
    
    try:
        mycur.execute('select exists(select * from emp1 where name="%s")'%name)
        for i in mycur:
            yes=i[0]
        if i[0]!=1:
            s_lable.config(text='Employee Not Exists!!')
        else:   
            mycur.execute('select * from emp1 where name="%s"'%name)
            mycur_l=[]
            for i in mycur:
                for j in range(len(i)):
                    mycur_l.append(i[j])
            v1.set(mycur_l[0])
            v2.set(mycur_l[2])
            v3.set(mycur_l[1])
            v4.set(mycur_l[3])
    except:
        conn.rollback()
    conn.close()    
    

def updatewindow():
    win2=Tk()
    win2.title('Update Employees')
    win2.minsize(width=500,height=200)
    win2.configure(bg='#F0FFFF')
    
    n_lable=Label(win2,text='Enter the Employee Name to be Update?',bg='#F0FFFF',font=('Times',15,'bold'))
    n_lable.place(x=20,y=20)
    
    v5=StringVar()
    e_name=Entry(win2,width=30,bd=2,font=('Times',16),textvariable=v5)
    e_name.place(x=20,y=70)

    def abcd():
        set_values(e_name.get())
        win2.destroy()
        
    n_submit=Button(win2,text='submit',command=abcd,font=('Times',15,'bold'))
    n_submit.place(x=20,y=120)
    win2.mainloop()
    

def sswindow():
    win3=Tk()
    win3.title('Employee Salary')
    win3.minsize(width=500,height=370)
    win3.configure(bg='#F0FFFF')
    
    n_lable=Label(win3,text='Enter the Employee Name ?',bg='#F0FFFF',font=('Times',15,'bold'))
    n_lable.place(x=20,y=20)
    

        
    v6=StringVar()
    s_name=Entry(win3,width=30,bd=2,font=('Times',16),textvariable=v6)
    s_name.place(x=20,y=70)
    
    def salDisplay():
        import mysql.connector
        conn=mysql.connector.connect(user='root',password='Ajit@0077',host='localhost',db='project')
        mycur=conn.cursor()    
        try:
            mycur.execute('select exists(select * from emp1 where name="%s")'%s_name.get())
            for i in mycur:
                yes=i[0]
            if i[0]!=1:
                sal_lable.config(text='Employee Not Exists!!')
            else:   
                mycur.execute('select salary from emp1 where name="%s"'%s_name.get())
                for i in mycur:
                    sal=i[0]
                sal_lable.config(text='%s\'s salary is %s!!'%(s_name.get(),sal))                
        except:
            conn.rollback()
        conn.close() 
        s_name.delete(0,END)

        
    s_submit=Button(win3,text='submit',command=salDisplay,font=('Times',15,'bold'))
    s_submit.place(x=20,y=120)
    
#     s_submit=Button(win3,text='clear',command=salclear,font=('Times',15,'bold'))
#     s_submit.place(x=100,y=120)
    
    sal_lable=Label(win3,width=30,bd=2,relief='ridge',height=3,bg='#F0FFFF',font=('Times',15,'bold'))
    sal_lable.place(x=20,y=220)
    
    win3.mainloop()

def dwindow():
    win4=Tk()
    win4.title('Employee Salary')
    win4.minsize(width=500,height=370)
    win4.configure(bg='#F0FFFF')
    
    n_lable=Label(win4,text='Enter the Employee Name ?',bg='#F0FFFF',font=('Times',15,'bold'))
    n_lable.place(x=20,y=20)
    
    def delclear():
        delete.set('')
        del_lable.config(text='')
        
    delete=StringVar()
    d_name=Entry(win4,width=30,bd=2,font=('Times',16),textvariable=delete)
    d_name.place(x=20,y=70)
    
    def delDisplay():
        import mysql.connector
        conn=mysql.connector.connect(user='root',password='Ajit@0077',host='localhost',db='project')
        mycur=conn.cursor()    
        try:
            mycur.execute('select exists(select * from emp1 where name="%s")'%d_name.get())
            for i in mycur:
                yes=i[0]
            if i[0]!=1:
                del_lable.config(text='Employee Not Exists!!')
            else:   
                mycur.execute('delete from emp1 where name="%s"'%d_name.get())
                conn.commit()
                del_lable.config(text='Employee Deleted!!')                
        except:
            conn.rollback()
        conn.close() 
        
    d_submit=Button(win4,text='submit',command=delDisplay,font=('Times',15,'bold'))
    d_submit.place(x=20,y=120)
    
    d_submit=Button(win4,text='clear',command=delclear,font=('Times',15,'bold'))
    d_submit.place(x=100,y=120)
    
    del_lable=Label(win4,width=30,bd=2,relief='ridge',height=3,bg='#F0FFFF',font=('Times',15,'bold'))
    del_lable.place(x=20,y=220)
    
    win4.mainloop()

def clear_all():
    tree.delete(*tree.get_children())   

    
def View():
        clear_all()
        import mysql.connector
        conn=mysql.connector.connect(user='root',password='Ajit@0077',host='localhost',db='project')
        mycur=conn.cursor()    
        mycur.execute('Select * from emp1')
        rows=mycur.fetchall()
        for row in rows:
            tree.insert("", 'end', values=(row))  
        conn.close()
        


l1=Label(win,text='Name',bg='#F0FFFF',font=('Times',15,'bold'))
l1.place(x=80,y=20)

v1=StringVar()
e1=Entry(win,width=30,bd=2,font=('Times',16),textvariable=v1)
e1.place(x=160,y=20)

l2=Label(win,text='Dept',bg='#F0FFFF',font=('Times',15,'bold'))
l2.place(x=80,y=80)

v2=StringVar()
cb=ttk.Combobox(win,width=28,font=('Times',16),textvariable=v2)
cb['values']=('Developer','HR','Sales','Manager','Finance')
cb.current(0)
cb.place(x=160,y=80)

l3=Label(win,text='MobNo',bg='#F0FFFF',font=('Times',15,'bold'))
l3.place(x=80,y=140)

v3=StringVar()
e3=Entry(win,width=30,bd=2,font=('Times',16),textvariable=v3)
e3.place(x=160,y=140)


l4=Label(win,text='Salary',bg='#F0FFFF',font=('Times',15,'bold'))
l4.place(x=80,y=200)

v4=StringVar()
e4=Entry(win,width=30,bd=2,font=('Times',16),textvariable=v4)
e4.place(x=160,y=200)

b1=Button(win,text='submit',command=disp,font=('Times',15,'bold'))
b1.place(x=80,y=260)

s_lable=Label(win,width=34,height=3,bg='#F0FFFF',font=('Times',15,'bold'))
s_lable.place(x=80,y=320)


ub=Button(win,text='Update',command=updatewindow,font=('Times',15,'bold'),width=12)
ub.place(x=80,y=450)

cb=Button(win,text='Clear',command=clear_all,font=('Times',15,'bold'),width=12)
cb.place(x=340,y=450)

sb=Button(win,text='Salary',command=sswindow,font=('Times',15,'bold'),width=12)
sb.place(x=80,y=550)

db=Button(win,text='Delete',command=dwindow,font=('Times',15,'bold'),width=12)
db.place(x=340,y=550)




# fetching
t_fetch=Label(win,text='Employee Details',bg='#F0FFFF',font=('Times',20,'bold'))
t_fetch.place(x=940,y=40)


reload=Button(win,text='Reload',command=View,font=('Times',15,'bold'),width=12)
reload.place(x=1250,y=650)

tree = ttk.Treeview(win, column=("Name", "Mobno", "Dept","Salary"), show='headings',height=25,selectmode='browse')
tree.place(x=650,y=100)

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="Name")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="Mobno")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="Dept")

tree.column("#4", anchor=tk.CENTER)

tree.heading("#4", text="salary")



win.mainloop()


# In[ ]:




