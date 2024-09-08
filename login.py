from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if UsernameEntry.get()=='' or PasswordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif UsernameEntry.get()=='venkat' and PasswordEntry.get()=='2007':
        messagebox.showinfo('Success','login successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Wrong Username or Password')

root=CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('login page')
image=CTkImage(Image.open('management.jpg'),size=(930,478))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headingLabel=CTkLabel(root,text='Employee Management System',bg_color='#162A31',text_color='white',font=('Goudy Old Style',40,'bold'))
headingLabel.place(x=200,y=20)

UsernameEntry=CTkEntry(root,placeholder_text='Enter Your Username',bg_color='#00628C',width=180)
UsernameEntry.place(x=400,y=150)

PasswordEntry=CTkEntry(root,placeholder_text='Enter Your Password',bg_color='#00628C',width=180,show='*')
PasswordEntry.place(x=400,y=180)

LoginButton=CTkButton(root,text='Login',bg_color='#00628C',cursor='hand2',command=login)
LoginButton.place(x=420,y=210)

root.mainloop()

