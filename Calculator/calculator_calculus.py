import tkinter as tk 
from tkinter import *
from sympy import Symbol,diff,integrate


class Calculator(tk.Frame):

    def __init__(self,root):
       
        super().__init__(root)
        self.root=root
        self.root.title("Calculator")
        root['bg']='cyan'
        self.root.geometry('280x493+450+500')
        self.create_widget()

       

    def create_widget(self):
        e=tk.Entry(self.root,width=35,borderwidth=5,font=('arial',10,'bold'))    
        e.grid(row=0,column=0,columnspan=3,padx=10,pady=40)

        
         
        def buttton_click(number):
            req=str(e.get())+str(number)
            e.delete(0,END)
            e.insert(0,req)

        def add():
            global first_var
            global sign
            root['bg']="green"
            first_num=e.get()
            first_var=(first_num)+"+"
            e.delete(0,END)
            e.insert(0,first_var)

        def sub():
            global first_var
            global sign
            first_num=e.get()
            root['bg']="red"
            first_var=(first_num)+"-"
            e.delete(0,END)
            e.insert(0,first_var)


        def into():
            global first_var
            global sign
            first_num=e.get()
            root['bg']="black"
            first_var=(first_num)+"*"
            e.delete(0,END)
            e.insert(0,first_var)


        def devide():
            global first_var
            global sign
            root['bg']="blue"
            first_num=e.get()
            first_var=(first_num)+"/"
            e.delete(0,END)
            e.insert(0,first_var)

        def clear():
            e.delete(0,END)                
         
      
        def integ():
            new =e .get()
            a=Symbol('a')
            present=integrate(new,a)
            e.delete(0,END)
            e.insert(0,present)

        def diffr():
            new =e .get()
            a=Symbol('a')
            present=diff(new,a)
            e.delete(0,END)
            e.insert(0,present)  
    
   
        
    
        button_1=tk.Button( self.root,text="1",padx=40,pady=20,command=lambda : buttton_click(1))
        button_2=tk.Button( self.root,text="2",padx=40,pady=20,command=lambda : buttton_click(2))
        button_3=tk.Button( self.root,text="3",padx=40,pady=20,command=lambda : buttton_click(3))
        button_4=tk.Button( self.root,text="4",padx=40,pady=20,command=lambda : buttton_click(4))
        button_5=tk.Button( self.root,text="5",padx=40,pady=20,command=lambda : buttton_click(5))
        button_6=tk.Button( self.root,text="6",padx=40,pady=20,command=lambda : buttton_click(6))
        button_7=tk.Button( self.root,text="7",padx=40,pady=20,command=lambda : buttton_click(7))
        button_8=tk.Button( self.root,text="8",padx=40,pady=20,command=lambda : buttton_click(8))
        button_9=tk.Button( self.root,text="9",padx=40,pady=20,command=lambda : buttton_click(9))
        button_0=tk.Button( self.root,text="0",padx=40,pady=20,command=lambda : buttton_click(0))
        button_a=tk.Button( self.root,text="a",padx=40,pady=20,command=lambda : buttton_click("a"))
        
        button_add=tk.Button( self.root,text="+",padx=39,pady=20,command= add )
        button_sub=tk.Button( self.root,text="-",padx=40.455,pady=20,command=sub)
        button_into=tk.Button( self.root,text="x",padx=40.12,pady=20,command=into)
        button_devide=tk.Button( self.root,text="/",padx=40,pady=20,command=diffr)
        button_clear=tk.Button( self.root,text="C",padx=39,pady=20,command=clear)
        button_integ=tk.Button( self.root,text="Integrate",padx=19.7,pady=20,command=integ)
        button_diff=tk.Button( self.root,text="dffrentiation",padx=9.5,pady=20,command=diffr)  
       
        button_1.grid(row=1,column=0)
        button_2.grid(row=1,column=1)     
        button_3.grid(row=1,column=2)
        button_integ.grid(row=4,column=1)
        button_diff.grid(row=4,column=2)
        button_a.grid(row=5,column=2)
       
        button_4.grid(row=2,column=0)
        button_5.grid(row=2,column=1)
        button_6.grid(row=2,column=2)
        button_add.grid(row=5,column=0)
        
        button_7.grid(row=3,column=0)
        button_8.grid(row=3,column=1)
        button_9.grid(row=3,column=2)
        button_sub.grid(row=6,column=0)
    
        button_0.grid(row=4,column=0)
        button_clear.grid(row=5,column=1)
        button_into.grid(row=6,column=1)
        button_devide.grid(row=6,column=2)










root=tk.Tk()
app=Calculator(root)
app.mainloop()