import requests
import bs4
from tkinter import messagebox
import tkinter as tk 

from PIL import ImageTk
import plyer
import datetime
import time
import threading

def get_html_data(url):
    data=requests.get(url)
    return data


def get_req_data_India():
    url='https://www.mygov.in/covid-19/'
    html_data=get_html_data(url)
    bs=bs4.BeautifulSoup(html_data.text,'html.parser')
    info_div = bs.find("div",class_="information_row")
    active_case=info_div.find("div",class_="iblock active-case")
    discharge_case=info_div.find("div",class_="iblock discharge")
    death_case=info_div.find("div",class_="iblock death_case")
    migrated_case=info_div.find("div",class_="iblock migared_case")

    Category=[active_case,discharge_case,death_case,migrated_case]
    data={}
    for cato in Category:
        count=cato.find("span",class_="icount").text
        text=cato.find("div",class_="info_label").text 
        data[text]=count
  
    return data

def for_notify():
    data = get_req_data_India()
    st=""
    i=1
    for d in data:
        if i==1:
            st= d + " : " + data[d] + "\n"
            i+=1  
        else:
            st= st + d + " : " + data[d] + "\n"
    
    return st     
            



class application(tk.Frame):

    def __init__(self,root):
        super().__init__(root)
        self.root=root
        self.root.title("Corona Tracker :  India  ")
        self.root.iconbitmap("health.ico")
        root['bg']="white"
        self.widget()
        self.root.geometry("820x304+200+50")
        self.root.resizable(False,False)

       

    def widget(self):
        r,c=2,1
        label_name=tk.Label(self.root,bg="white",text="Total Cases" ,font=f)
        label_name.grid(row=1,column=c)
        label_name=tk.Label(self.root,bg="white",text=" : " ,font=f)
        label_name.grid(row=1,column=c+1)
        label_count=tk.Label(self.root,bg="white",text=int(Details['Active Cases'])+int(Details['Cured / Discharged ']),font=f)
        label_count.grid(row=1,column=c+2)
        for det in Details:
 
            label_name=tk.Label(self.root,bg="white",text=det ,font=f)
            label_name.grid(row=r,column=c)
            label_name=tk.Label(self.root,bg="white",text=" : " ,font=f)
            label_name.grid(row=r,column=c+1)
            label_count=tk.Label(self.root,bg="white",text=Details[det],font=f)
            label_count.grid(row=r,column=c+2)
            r+=1
        
      

        def refresh():
            Detail=get_req_data_India()
            self.widget()
            messagebox.showinfo("Refreshed","You have been refreshed")
          
             
        Refresh=tk.Button(self.root,text="Refresh",height=1,width=30,font=f,relief='solid',bg="white",command=refresh)
        Refresh.grid(row=7,column=1,columnspan=3)    
     


def Donate():
    donate=tk.Toplevel()
    donate.title("Donate to Goverment")
    donate.iconbitmap("health.ico")
    image1=ImageTk.PhotoImage(file="UPIQR1.jpeg")
    label1_image=tk.Label(donate,image=image1,borderwidth=2)
    label1_image.grid(row=0,column=0)  
    donate.mainloop()          

def notify():
    while(True):
        plyer.notification.notify(
            title="Corona Tracker",
            message=for_notify(),
            timeout=10,
            app_icon='health.ico',
        )
        time.sleep(3600)




root=tk.Tk()
f=('arials',20,'bold')
Details=get_req_data_India()
image=ImageTk.PhotoImage(file="indias1.jpg")
label_image=tk.Label(root,image=image,borderwidth=2)
label_image.grid(row=0,column=0,rowspan=8)
Donate=tk.Button(root,text=" Donate to Government ",bg="white",font=f,relief='solid',width=30,command=Donate)
Donate.grid(row=0,column=1,columnspan=3,padx=3)
app=application(root)

th1=threading.Thread(target=notify)
th1.setDaemon(True)
th1.start()
app.mainloop()
