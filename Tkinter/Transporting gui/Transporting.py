from tkinter import *
from tkinter import ttk
import datetime
import time
import tkinter.messagebox
import sqlite3





class school_portal():
    dbname='Transport.db'

    def __init__(self,root):
        self.root=root
        self.root.title('Transporting Data')
        ##-----------------logo------------------
        self.photo=PhotoImage(file='shipping-and-delivery.png')
        self.photo = self.photo.subsample(3, 3)
        self.label=Label(image= self.photo)
        self.label.grid(row=0,column=0)
        ##----------------TITLE------------------
        self.labell=Label(font=('arial',15,'bold') ,text='Transportation Service',fg='dark blue')
        self.labell.grid(row=8,column=0)
        ##--------------my name added at last-----------------
        self.labell = Label(font=('arial', 8, 'bold'), text='MS production', fg='dark green')
        self.labell.grid(row=11, column=0,columnspan=4)

        ##-----FRAME--TO--ADD--NEW--RECORD-------
        frame=LabelFrame(self.root,font=('arial',12,'bold'), text='Add new record')
        frame.grid(row=0,column=2)

        Label(frame,text='Company:').grid(row=2, column=1,sticky=W)
        self.Company=Entry(frame)
        self.Company.grid(row=2,column=2)

        Label(frame, text='Ingredientes:').grid(row=3, column=1, sticky=W)
        self.Ingredientes = Entry(frame)
        self.Ingredientes.grid(row=3, column=2)

        Label(frame, text='Weight(in Kg):').grid(row=4, column=1, sticky=W)
        self.Weight = Entry(frame)
        self.Weight.grid(row=4, column=2)

        Label(frame, text='E(Exported) or I(Imported):').grid(row=5, column=1, sticky=W)
        self.EorI = Entry(frame)
        self.EorI.grid(row=5, column=2)

        Label(frame, text='Vehicle number ').grid(row=6, column=1, sticky=W)
        self.Vehicle = Entry(frame)
        self.Vehicle.grid(row=6, column=2)

        ##---------------Button----------------
        ttk.Button(frame,text='Add record',command= self.add).grid(row=7,column=2)

        ##-------MESSAGE NEED TO DISPLAY-------
        self.message=Label(text='',fg='red')
        self.message.grid(row=8,column=2)


        ##---------DATABASE TABLE--------------
        self.tree = ttk.Treeview(height=10,column=['','','','',''])
        self.tree.grid(row=9,column=0,columnspan=3)
        self.tree.heading('#0',text='ID')
        self.tree.column('#0',width=50)
        self.tree.heading('#1', text='COMPANY')
        self.tree.column('#1', width=100)
        self.tree.heading('#2', text='INGREDIENTES')
        self.tree.column('#2', width=100)
        self.tree.heading('#3', text='WEIGHT')
        self.tree.column('#3', width=100)
        self.tree.heading('#4', text='E or I')
        self.tree.column('#4', width=80)
        self.tree.heading('#5', text='VEHICLE NO.')
        self.tree.column('#5', width=120,stretch=False)

        #-------------TIME AND DATE-------------------
        def trc():
            d=datetime.datetime.now()
            Today='{:%B %d,%Y}'.format(d)
            mytime=time.strftime('%I:%M:%S %p')
            self.lat.config(text=(mytime +2*'\t'+ Today))
            self.lat.after(100,trc)

        self.lat = Label(font=('arail',18,'bold'),fg='dark blue')
        self.lat.grid(row=10,column=0,columnspan=3)
        trc()

        menu=Menu()
        file=Menu()
        root.config(menu=menu)

        menu.add_cascade(label='File',menu=file)
        menu.add_cascade(label='Add',command= self.add)
        menu.add_cascade(label='Delete',command=self.dele)
        menu.add_cascade(label='Edit',command=self.edit_box)
        menu.add_cascade(label='Help',command=self.help)
        menu.add_cascade(label='Exit',command=self.exit)

        file.add_command(label='Add Record',command= self.add)
        file.add_command(label='Delete Record',command=self.dele)
        file.add_command(label='Edit Record',command=self.edit_box)
        file.add_separator()
        file.add_command(label='Total amount of ingredientes')
        file.add_command(label='help')
        file.add_command(label='Exit')

        self.viewing_db()


    #---------------DATABASE CONNECTIVITY--------------
    def rundb(self,query,parameters=()):
        with sqlite3.connect(self.dbname) as con:
          cursor =con.cursor()
          query_result=cursor.execute(query,parameters)
          con.commit()
        return query_result

    #---------------Viewing database-------------------
    def viewing_db(self):
        records = self.tree.get_children()
        for elementes in records:
           self.tree.delete(elementes)
        query = 'SELECT * FROM transpotingdata'
        db_table = self.rundb(query)
        for data in db_table:
           self.tree.insert('',1000,text=data[0],values=data[1:])
    #---------------checking that all fields are filled--------
    def validation(self):
        return len(self.Company.get()) !=0 and len(self.Ingredientes.get()) !=0 and len(self.Weight.get()) !=0 and \
        len(self.EorI.get()) != 0 and len(self.Vehicle.get()) !=0

    #---------------Adding a record----------------------------
    def add(self):
        if self.validation():
            query = 'INSERT INTO transpotingdata VALUES (NULL,?,?,?,?,?)'
            parameters =(self.Company.get(),self.Ingredientes.get(),self.Weight.get(),self.EorI.get(),self.Vehicle.get() )
            self.rundb(query,parameters)
            self.message['text']='{} veghicle number with {} matarial recorded '.format(self.Vehicle.get(),self.Ingredientes.get())

            self.Company.delete(0,END)
            self.Ingredientes.delete(0, END)
            self.Weight.delete(0, END)
            self.EorI.delete(0, END)
            self.Vehicle.delete(0, END)

        else:
            self.message['text']='Fill all the detail with appropirate data type'
        self.viewing_db()

    #------------------delete a record---------------
    def delete(self):
        self.message['text']= ''
        try:
            self.tree.item(self.tree.selection())['values'][1]
        except IndexError as e:
            self.message['text']='Please,select a record to delete'
            return
        self.message['text']=''
        num=self.tree.item(self.tree.selection())['text']
        query='DELETE FROM transpotingdata WHERE ID =?'
        self.rundb(query,(num,))
        self.message['text']='Record {} is deleted'.format(num)
        self.viewing_db()

    def dele(self):
        de=tkinter.messagebox.askquestion('Delete Record','Sure you want wo delete this')
        if de == 'yes':
            self.delete()

    #-------------------edit a record----------------------
    def edit_box(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Please,select a record to Edit'
            return


        Cname=self.tree.item(self.tree.selection())['values'][0]
        Ingre=self.tree.item(self.tree.selection())['values'][1]
        weigh=self.tree.item(self.tree.selection())['values'][2]
        eori =self.tree.item(self.tree.selection())['values'][3]
        regn =self.tree.item(self.tree.selection())['values'][4]

        self.edit_root=Toplevel()
        self.edit_root.title('Edit Records')

        Label(self.edit_root,text='Old Company name').grid(row=0 ,column=1,sticky=W)
        Entry(self.edit_root,textvariable=StringVar(self.edit_root,value=Cname),state='readonly').grid(row=0 ,column =2)
        Label(self.edit_root, text='New Company name ').grid(row=1, column=1, sticky=W)
        new_Cname=Entry(self.edit_root)
        new_Cname.grid(row=1,column=2)

        Label(self.edit_root, text='Old Ingredient Entry').grid(row=2, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root,value= Ingre), state='readonly').grid(row=2, column=2)
        Label(self.edit_root, text='New Ingredient Entry ').grid(row=3, column=1, sticky=W)
        new_Ingre = Entry(self.edit_root)
        new_Ingre.grid(row=3, column=2)

        Label(self.edit_root, text='Old Weight Entry').grid(row=4, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root,value= weigh), state='readonly').grid(row=4, column=2)
        Label(self.edit_root, text='New Weight Entry ').grid(row=5, column=1, sticky=W)
        new_Weigh = Entry(self.edit_root)
        new_Weigh.grid(row=5, column=2)

        Label(self.edit_root, text='Previously Ex or Im').grid(row=6, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root,value= eori), state='readonly').grid(row=6, column=2)
        Label(self.edit_root, text='Now Actualy ').grid(row=7, column=1, sticky=W)
        new_Eori = Entry(self.edit_root)
        new_Eori.grid(row=7, column=2)

        Label(self.edit_root, text='Wrong Puted Vehicle Number').grid(row=8, column=1, sticky=W)
        Entry(self.edit_root, textvariable=StringVar(self.edit_root,value= regn), state='readonly').grid(row=8, column=2)
        Label(self.edit_root, text='Correct Vehicle number').grid(row=9, column=1, sticky=W)
        new_regn = Entry(self.edit_root)
        new_regn.grid(row=9, column=2)

        Button(self.edit_root,text='Save Changes',
               command= lambda:self.edit_records(new_Cname.get(),Cname,new_Ingre.get(),Ingre,new_Weigh.get(),weigh,new_Eori.get(),eori,new_regn.get(),regn)).grid(row = 10, column=2,sticky=W)


        self.edit_root.mainloop()

    def edit_records(self,new_Cname,Cname,new_Ingre,Ingre,new_Weigh,weigh,new_Eori,eori,new_regn,regn):
            query='UPDATE transpotingdata SET Company=?,Ingredientes=?,Weight=? ,Transfer=?, Vehicle=? WHERE Company=? AND Ingredientes=? AND Weight=? AND transfer=? AND Vehicle=?'
            parameters=(new_Cname,new_Ingre,new_Weigh,new_Eori,new_regn,Cname,Ingre,weigh,eori,regn)
            self.rundb(query,parameters)
            self.edit_root.destroy()
            self.message['text']='{} company with {} ingredientes details were changed '.format(new_Cname,new_Ingre)
            self.viewing_db()

    def edit(self):
           ab= tkinter.messagebox.askquestion('Edit Record','Want to Edit a Record')
           if ab == 'yes':
               self.edit_box()
    #--------------Helpdesk and exit--------------------
    def help(self):
        tkinter.messagebox.showinfo('Helpdesk','Report Sent company email : mayanksahu22107@gmail.com ')

    def exit(self):
        g=tkinter.messagebox.askquestion('Exit','Do you want to close the app')
        if g == 'yes':
            root.destroy()



if __name__=='__main__':
    root=Tk()
    root.geometry('555x490+500+200')
    application=school_portal(root)
    root.mainloop()
