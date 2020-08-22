import tkinter as tk 
from math import ceil
from pygame import mixer
from tkinter.ttk import Progressbar
from tkinter import ttk,filedialog,StringVar,messagebox
import youtube_dl
#from youtube_dl import YoutubeDL
from mutagen.mp3 import MP3
#import datetime
import os

root=tk.Tk()
root.title("Python music player : Offline")
root.geometry("570x850+500+100")
root.resizable(False,False)
root.iconbitmap("images//music.ico")
mixer.init()

mixer.music.set_volume(0.5)

red_image=tk.PhotoImage(file="images//red.png")
theme_image=tk.PhotoImage(file="images//theme.png")
green_image=tk.PhotoImage(file="images//green.png")
music_image=tk.PhotoImage(file="images//heart.png")
start_image=tk.PhotoImage(file="images//power.png")
stop_image=tk.PhotoImage(file="images//off.png")
volume_add_image=tk.PhotoImage(file="images//add_volume.png")
volume_sub_image=tk.PhotoImage(file="images//sub_volume.png")
mute_image=tk.PhotoImage(file="images//Mute.png")
unmute_image=tk.PhotoImage(file="images//full_volume.png")

searh_image=tk.PhotoImage(file="images//search.png")
browse_image=tk.PhotoImage(file="images//dvd.png")
play_image=tk.PhotoImage(file="images//play-button.png")
pause_image=tk.PhotoImage(file="images//pause.png")

quit_image=tk.PhotoImage(file="images//exit.png")

volume_stat=mute_image
state=red_image
condition=start_image
prev_volume=0
dd="Sample.mp3"
search_or_browse=browse_image
doin = play_image
audiotrack=StringVar()
audiotrack.set(dd)
current_pos=0
SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Downloads'




def brow():
    global dd,audiotrack,ProgressbarMusic
   
      
    if state == red_image:  
        
        if messagebox.askyesno("Browse","Want to open  your downloaded music "):
            try:
                dd=filedialog.askopenfilename(initialdir=SAVE_PATH,
                                              title='Select file',
                                              filetype=(('MP3','*mp3'),('WAV','*wav'),('*mp4','MP4'))      )
            except:
                messagebox.showerror("Error","You havent downloaded any thing from us")    
        else:
            try:
                dd=filedialog.askopenfilename(initialdir='C:Users/Public/Music',
                                              title='Select file',
                                              filetype=(('MP3','*mp3'),('WAV','*wav'),('*mp4','MP4'))      )
            except:
                    dd=filedialog.askopenfilename(
                                                  title='Select file',
                                                  filetype=(('MP3','*mp3'),('WAV','*wav'),('*mp4','MP4'))      )
        audiotrack.set(dd)
          
    else:
        if messagebox.askokcancel("Download","Your Music Will be stopped "):
            mixer.music.stop()
            if condition==stop_image:
                power_fun()
            params={
            'format' : 'bestaudio/best',
            'postprocessors' : [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192',
                 
            }]
              ,
            'outtmpl':SAVE_PATH + '/%(title)s.%(ext)s',
            }
            music=youtube_dl.YoutubeDL(params)
        
            try:
                
                music.download([e.get()])
            
                messagebox.showinfo("Downloads","Your Music has been downloaded")    
            
            except: 
                messagebox.showerror("Error","May be internet is not avilable or may be yout link is wrong")
        
                                        
   
  


        
    




def play():
    global doin,ProgressbarMusic

    if doin == play_image:
        doin=pause_image
        txt="Pause"
        play_button.config(image=doin, text=txt)
    
        mixer.music.unpause()
        
        def teer():
            current_pos=mixer.music.get_pos()/1000
            ProgressbarMusic['value']=current_pos
            ProgressbarMusic.after(200,teer)
        teer()
        

    else:
        doin=play_image
        txt="Play"
        play_button.config(image=doin, text=txt)
        mixer.music.pause()
        current_pos=mixer.music.get_pos()//1000
        ProgressbarMusic['value']=current_pos
 

def changing(color):
    root['bg']=color
    Theme_button.config(bg=color,activebackground=color)
    state_button.config(bg=color,activebackground=color)
    music_logo.config(bg=color)
    volume_down_button.config(bg=color,activebackground=color)
    volume_up_button.config(bg=color,activebackground=color)
    power_button.config(bg=color,activebackground=color)
    play_button.config(bg=color,activebackground=color)
    mute_button.config(bg=color,activebackground=color)
    exit_button.config(bg=color,activebackground=color)
    load_button.config(bg=color,activebackground=color)
    slider_label.config(bg=color)
    love_label.config(bg=color)
    label_red.config(bg=color)

def changing_font(color):
    
    Theme_button.config(fg=color)
    state_button.config(fg=color)
    music_logo.config(fg=color)
    volume_down_button.config(fg=color)
    volume_up_button.config(fg=color)
    power_button.config(fg=color)
    play_button.config(fg=color)
    mute_button.config(fg=color)
    exit_button.config(fg=color)
    load_button.config(fg=color)
    slider_label.config(fg=color)
    love_label.config(fg=color)
    e.config(fg=color)
    slider_label.config(fg=color)
    love_label.config(fg=color)
    label_red.config(fg=color)


def change_theme():
    T=tk.Toplevel()
    T.title("Change Theme")
    T.iconbitmap("images//music.ico")
    T.geometry("200x100")
    def ok():
       changing(Theme_label.get())
       T.destroy()
    bg_label=tk.Label(T,text="Enter The Color for background",font=('poppins',10))
    bg_label.grid(row=0,column=0,columnspan=2)   
    Theme_label=tk.Entry(T,width=20,border=3)
    Theme_label.grid(row=1,column=0)
    ok_button=tk.Button(T,text="Change",bg="lightskyblue" ,command=ok)
    ok_button.grid(row=1,column=1)
    def ok_f():
       changing_font(font_label.get())
       T.destroy()
    fg_label=tk.Label(T,text="Enter The Color for Font",font=('poppins',10))
    fg_label.grid(row=2,column=0,columnspan=2)    
    font_label=tk.Entry(T,width=20,border=3)
    font_label.grid(row=3,column=0)
    ok_bbutton=tk.Button(T,text="Change",bg="lightskyblue", command=ok_f)
    ok_bbutton.grid(row=3,column=1)

   

def state_fun(): 
    global state
   
    if state==red_image:
       state=green_image
       txt="Online"
       root.title("Python music player : Online  (Downloads only)")
       state_button.config(image=state,text=txt)
       tyyt=searh_image
       tyyt_txt="Search"
       load_button.config(image=tyyt,text=tyyt_txt)
       label_red.config(text=" Paste url here :")
    else:
        e.grid()
        state=red_image
        txt="Offline"
        root.title("Python music player : Offline")
        state_button.config(image=state,text=txt)
        tyyt=browse_image
        tyyt_txt="Browse"
        load_button.config(image=tyyt,text=tyyt_txt)
      
       
        label_red.config(text=" path : ")


def power_fun():
    global condition ,doin,ProgressbarMusic

    if condition == start_image:
        condition=stop_image
        txt="Stop"
        power_button.config(image=condition, text=txt)
        doin=pause_image
        txt="Pause"
        play_button.config(image=doin, text=txt)
        
         
        mixer.music.load(dd)
        mixer.music.play()
        song= MP3(dd)
        total_length=int(song.info.length)
        ProgressbarMusic['maximum']=total_length  
        
        def teer():
            current_pos=mixer.music.get_pos()/1000
            ProgressbarMusic['value']=current_pos
            ProgressbarMusic.after(200,teer)
        teer()
        start_slider()
        IntroLabel_effetct()

    else:
        condition=start_image
        txt="Start"
        power_button.config(image=condition, text=txt)
        doin=play_image
        txt="Play"
        play_button.config(image=doin, text=txt)
        
        mixer.music.stop()
        ProgressbarMusic['value']=0
    


def mute():
    
    global volume_stat,prev_volume
    
    if volume_stat == mute_image:
       prev_volume=mixer.music.get_volume() 
       volume_stat=unmute_image
       txt = "Unmute"
       mute_button.config(image=volume_stat,text=txt)
       mixer.music.set_volume(0)
       new=ceil(mixer.music.get_volume()*100)
         
       ProgressbarVolume.config(value=new)
    else:
        volume_stat=mute_image
        txt="Mute"   
        mute_button.config(image=volume_stat,text=txt)
        mixer.music.set_volume(prev_volume)
        new=ceil(mixer.music.get_volume()*100)
          
        ProgressbarVolume.config(value=new)


def volume_up():
    global volume_stat
  
    if volume_stat == unmute_image:
        volume_stat=mute_image
        txt="Mute"   
        mute_button.config(image=volume_stat,text=txt)
        mixer.music.set_volume(prev_volume)
        new=ceil(mixer.music.get_volume()*100)
         
        ProgressbarVolume.config(value=new)

    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol+0.05) 
    new=ceil(mixer.music.get_volume()*100)
    ProgressbarVolume.config(value=new)    

def volume_down():
    global volume_stat
  
    if volume_stat == unmute_image:
        volume_stat=mute_image
        txt="Mute"   
        mute_button.config(image=volume_stat,text=txt)
        mixer.music.set_volume(prev_volume)
        new=ceil(mixer.music.get_volume()*100)
         
        ProgressbarVolume.config(value=new)    
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol-0.05)        
    new=ceil(mixer.music.get_volume()*100)
         
    ProgressbarVolume.config(value=new)




def quit_fun():
  

   if messagebox.askyesno("Quit","Do you want to quit Python Music Plater"):
      root.destroy()
       
   

music_logo=tk.Label(root,image=music_image)
music_logo.grid(row=2,column=1,columnspan=3)

e=tk.Entry(root,width=55,border=3,textvariable=audiotrack)
e.grid(row=1,column=1,padx=20,columnspan=3)



Theme_button=tk.Button(root,image=theme_image,text="Themes", compound="top",border=0, command=change_theme)
Theme_button.grid(row=0,column=0,pady=20)

state_button=tk.Button(root, image=state, text="Offline",compound="top",border=0,command=state_fun)
state_button.grid(row =0,column=2,pady=20)

power_button=tk.Button(root,image=condition, text="Start",compound="top",border=0,command=power_fun)
power_button.grid(row=0,column=1)

volume_up_button=tk.Button(root,image=volume_add_image,text="Vol +",compound="top",border=0,command=volume_up)
volume_down_button=tk.Button(root,image=volume_sub_image,text="Vol -",compound="top",border=0,command=volume_down,)
volume_up_button.grid(row=8,column=4,ipadx=10,padx=10)
volume_down_button.grid(row=8,column=0,padx=10)

mute_button=tk.Button(root,image=volume_stat,text="Mute",compound="top",border=0,command=mute)
mute_button.grid(row=7,column=0,pady=30)



load_button=tk.Button(root,image=browse_image,text="Browse",compound="top",border=0,command=brow)
load_button.grid(row=0,column=3)

play_button=tk.Button(root,image=doin,text="Play",compound="top",border=0,command=play)
play_button.grid(row=7,column=4,pady=30)


exit_button=tk.Button(root,image=quit_image,text="Quit",compound="top",border=0,command=quit_fun)
exit_button.grid(row=0,column=4)

label_red=tk.Label(root,text=" path : ")
label_red.grid(row=1,column=0)


###############################################################################################################
ss=""
def start_slider():
    
    global ss
    ss=""
    x=1
    text=""
    for d in dd:
        if d == "/":
            ss=""
        else :
            ss+=d
    for i in ss:
        text+=i
        if x==20:
            break
        x+=1
    slider_label.config(text="Playing now :"+text)

slider_label=tk.Label(root,text=ss,fg="#c70039",width=30,font=('poppins',10,'bold'))
slider_label.grid(row=7,column=1,columnspan=3,pady=10)



sd="Made with 💗love💗  in Bhilai"
count=0
text_love=""
love_label=tk.Label(root,text=text_love,fg="#c70039",font=('poppins',10,'bold'))
love_label.grid(row=9,column=0,columnspan=5,pady=10)
def IntroLabel_effetct():
    global count,text_love
    if count>=len(sd):
       count=-1
       text_love=""
       love_label.config(text=text_love)
    else:
        text_love+=sd[count]
        love_label.config(text=text_love)
    count+=1
    love_label.after(400,IntroLabel_effetct) 

################################################################################################################


current_volume=ceil(mixer.music.get_volume()*100)

ProgressbarLabel=tk.Label(root,bg='lightskyblue',width=2)
ProgressbarLabel.grid(row=8,column=1,columnspan=3,pady=20)

ProgressbarVolume=Progressbar(ProgressbarLabel,orient=tk.HORIZONTAL,style="lightskyblue.Horizontal.TProgressbar",mode='determinate',value=current_volume,length=350)
ProgressbarVolume.grid(row=0,column=0,ipadx=10,ipady=20)

ProgressbarLabel_music=tk.Label(root,bg='lightskyblue',width=80)
ProgressbarLabel_music.grid(row=5,column=0,columnspan=5)

ProgressbarMusic=Progressbar(ProgressbarLabel_music,orient=tk.HORIZONTAL,style="lightskyblue.Horizontal.TProgressbar",mode='determinate',value=current_pos,length=440)
ProgressbarMusic.grid(row=0,column=0)

s = ttk.Style()
s.theme_use('alt')
s.configure("lightskyblue.Horizontal.TProgressbar", foreground='#c70039', background='#c70039')


messagebox.showinfo("Introduction ","In online mode you can only download songs by providing link and in offline you can Play song Moreover when you select a song to play you have to first stop the previous song then start so that new song can be load")
root.mainloop()
