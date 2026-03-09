#import all necessary modules

import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Tk, Text
from pygame import mixer
import pickle
import json
import spotipy
import webbrowser
from prettytable import PrettyTable

#code to implement spotify database

'''
clientID = 'Your client ID'
clientSecret = 'Your client secret'
redirect_url = 'Your redirect url'
'''

oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_url)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()

#creating main window

root = Tk()
root.title("NJ Music Player")
root.geometry("1300x800+290+10")
root.configure(background='#333333')
root.resizable(False, False)
mixer.init()

#defining functions for searching,adding and playing music files

def o_table():
     try:
          o_file=open("history.dat","rb")
          myTab = PrettyTable(["Song Name", "Artist", "Link"])
          try:
               while True:
                    history=pickle.load(o_file)
                    song_name=history[0]
                    if len(song_name)>=30:
                         myTab.add_row([song_name[0:30],history[1],history[2]])
                    else:
                         myTab.add_row([history[0],history[1],history[2]])
          except EOFError:
               pass
          o_file.close()
          return myTab
     except FileNotFoundError:
          messagebox.showerror('Error','Binary File Not Found')

def d_table():
     try:
          o_file=open("songs.dat","rb")
          myTab = PrettyTable(["Song Name"])
          try:
               while True:
                    history=pickle.load(o_file)
                    myTab.add_row([history[0]])
          except EOFError:
               pass
          o_file.close()
          return myTab
     except FileNotFoundError:
          messagebox.showerror('Error','Binary File Not Found')

def Search():
     try:
          o_file=open("history.dat","ab")
          on_search = edit.get()
          if on_search=="":
               messagebox.showerror('Error','No Song Searched')
          else:
               results = spotifyObject.search(on_search, 1, 0, "track")
               songs_dict = results['tracks']
               song_items = songs_dict['items']
               song = song_items[0]['external_urls']['spotify']
               webbrowser.open(song)
               for item in results['tracks']['items']:
                    name=item['name']
                    artist=item['artists'][0]['name']
                    history=[name,artist,song]
                    pickle.dump(history,o_file)
          o_file.close()
     except FileNotFoundError:
          messagebox.showerror('Error','Binary File Not Found')
          
def AddMusic():
     try:
          path = filedialog.askdirectory()
          d_file=open("songs.dat","ab")
          if path:
               os.chdir(path)
               songs = os.listdir(path)

               for song in songs:
                    if song.endswith(".mp3"):
                         Playlist.insert(END, song)
                         songlist=[]
                         songlist.append(song+"\n")
                         pickle.dump(songlist,d_file)
          d_file.close()
     except FileNotFoundError:
          messagebox.showerror('Error','Binary File Not Found')
    
def PlayMusic():
     Music_Name = Playlist.get(ACTIVE)
     if Music_Name == "":
          messagebox.showerror('Error', 'No Directory Selected!')
     else:
          mixer.music.load(Playlist.get(ACTIVE))
          mixer.music.play()
          try:
               o_file=open("songs.dat","ab")
               history=[Playlist.get(ACTIVE),"(From directory)"+"\n"]
               pickle.dump(history,o_file)
               l = Label(root, text ="Now playing: ")
               l.config(font =("Consolas", 17,"bold"),anchor="center",
                        height=1,width=29,bg="#495057",fg="#b6afa8")
               l.place(x=250,y=513)
               l2 = Label(root, text = Playlist.get(ACTIVE))
               l2.config(font =("Consolas", 17,"bold"),anchor="center",
                         height=1,width=60,bg="#495057",fg="#b6afa8")
               l2.place(x=30,y=563)
               o_file.close()
          except FileNotFoundError:
               messagebox.showerror('Error','Binary File Not Found')

#defining functions to read and display binary files

def Showimported():
     new= Toplevel(root)
     new.geometry("570x650")
     new.resizable(False, False)
     new.title("Imported")
     new.configure(bg = "#343A40")
     Label(new, text="All Imported Songs",
           font=('Consolas 20 bold'),
           bg = "#343A40", fg="#ADB5BD").pack(pady=30)
     T = Text(new, width=130,height=23,
              font=("Consolas", 15),
              bg="#212529", fg="#ADB5BD")
     T.pack(padx=20)
     column=d_table()
     T.insert(END,column)

def Showhistory():
     new= Toplevel(root)
     new.geometry("1235x700")
     new.resizable(False, False)
     new.title("History")
     new.configure(bg = "#343A40")
     Label(new, text="History",
           font=('Consolas 20 bold'),
           bg = "#343A40", fg="#ADB5BD").pack(pady=30)
     T = Text(new, width=196,height=43,
              font=("Consolas", 15),
              bg="#212529", fg="#ADB5BD")
     T.pack(padx=20)
     column=o_table()
     T.insert(END,column)

def About():
     try:
          a_file=open("info.dat","rb")
          new= Toplevel(root)
          new.geometry("1000x650")
          new.resizable(False, False)
          new.title("About The Project")
          new.configure(bg = "#343A40")
          Label(new, text="About",
                font=('Helvetica 17 bold'),
                bg = "#343A40", fg="#ADB5BD").pack(pady=30)
          T = Text(new, height = 350, width = 200,
                   bg="#212529", fg="#ADB5BD")
          T.pack()
          try:
               while True:
                    history=pickle.load(a_file)
                    T.insert(END,history[0])
          except EOFError:
               pass
          a_file.close()
     except FileNotFoundError:
          messagebox.showerror('Error','Binary File Not Found')

#defining function for volume controls

def volumedown():
    mixer.music.set_volume(mixer.music.get_volume() - 0.1)

def volumeup():
    mixer.music.set_volume(mixer.music.get_volume() + 0.1)
    
#creating sections of main window

image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

lower_frame = Frame(root , bg = "#343A40",
                    width = 1300 , height = 230 )
lower_frame.place ( x = 0 , y = 600)

upper_frame = Frame(root , bg ="#495057",
                    width = 1300 , height = 620)
upper_frame.place( x = 0 , y = 0)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=950, y=33,
                  width=350, height=380)

Online_Frame_Music = Frame(root, bd=2, relief=RIDGE)
Online_Frame_Music.place(x=950, y=480,
                         width=350, height=320)

Scroll_p = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=350, font=("Times new roman", 10),
                   bg="#212529", fg="#ADB5BD", selectbackground="#524A42", cursor="hand2", bd=0, yscrollcommand=Scroll_p.set)
Scroll_p.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)
Scroll_o = Scrollbar(Online_Frame_Music)
Online = Listbox(Online_Frame_Music, width=350, font=("Times new roman", 10),
                 bg="#212529", fg="#ADB5BD", selectbackground="#524A42", cursor="hand2", bd=0, yscrollcommand=Scroll_o.set)
Scroll_o.config(command=Playlist.yview)
Scroll_o.pack(side=RIGHT, fill=Y)
Online.pack(side=RIGHT, fill=BOTH)

Pic = PhotoImage(file="mid.png")
Label(root, image=Pic,bg="#495057").place(x=290, y=133, width=320, height=326)

#creating buttons and entry field

Buttonvolumedownimg= PhotoImage(file="volume-down.png")
Buttonvolumedown = Button(image=Buttonvolumedownimg, bg="#343A40", bd=0,
                          height = 60, width =40)
Buttonvolumedown.configure(command=volumedown)
Buttonvolumedown.place(x=20,y=687)

Buttonvolumeupimg= PhotoImage(file="volume.png") 
Buttonvolumedown = Button(image=Buttonvolumeupimg, bg="#343A40", bd=0,
                          height = 60, width =40)
Buttonvolumedown.configure(command=volumeup)
Buttonvolumedown.place(x=150,y=687)

ButtonPlay = PhotoImage(file="play1.png")
Button(root, image=ButtonPlay, bg="#343A40", bd=0,
       height = 60, width =60,
       command=PlayMusic).place(x=375, y=687)

ButtonPause = PhotoImage(file="pause1.png")
Button(root, image=ButtonPause, bg="#343A40", bd=0,
       height = 60, width =60,
       command=mixer.music.pause).place(x=450, y=687)

ButtonMenu = PhotoImage(file="info.png")
Button(root, image=ButtonMenu, bg="#495057", bd=0,
       height = 32, width =32,
           command=Showimported).place(x=20, y=20)

ButtonHistory = PhotoImage(file="history.png")
Button(root, image=ButtonHistory, bg="#495057", bd=0,
       height = 32, width =32,
           command=Showhistory).place(x=20, y=70)

ButtonAbout = PhotoImage(file="about.png")
Button(root, image=ButtonAbout, bg="#495057", bd=0,
       height = 32, width =32,
           command=About).place(x=20, y=120)

Button(root, text="Browse Music", width=38, height=1, font=("Consolas",12, "bold"),
       fg="Black", bg="#FFFFFF", command=AddMusic).place(x=950, y=0)

Button(root, text='Search Online',width=38,height=1, font=("Consolas",12,"bold"),
       fg="Black", bg="#FFFFFF",command=Search).place(x=950,y=447)

edit = Entry(root, width=29,font=("calibri",17))
edit.pack(side=LEFT, fill=BOTH, expand=1)
edit.place(x=950,y=413)


#execute Tkinter

root.mainloop()