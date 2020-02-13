from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time




def rootScreen():
    global root

    root = Tk()
    root.title('Codechat')
    root.iconbitmap('codechat.png')
    root.geometry('800x400+300+150')
    root.resizable(False, False)
    root.configure(background='#2A3D45')
    #root.overrideredirect(True)
    root.wm_attributes('-alpha', 1)

    Label(text='', width='400', height='2',bg ='#2A3D45').pack()
    Label(text='Codechat', width='400', height='1', bg ='#2A3D45', fg='white', font=('Arial', 30)).pack()
    Label(text='by HoruSoft', width='400', height='1', bg ='#2A3D45', fg='white', font=('Arial', 10)).pack()
    Label(text='', width='400', height='2',bg ='#2A3D45' ).pack()

    Button(text='Login',  width='30', height='2', command=loginScreen, font=('Arial', 15)).pack()
    Button(text='Create Account', width='30', height='2', command=root.quit, font=('Arial', 15)).pack()
    Label(text='', width='400', height='2', bg='#2A3D45' ).pack()
    Button(text='Quit', width='15', height='2', command=root.quit, font=('Arial', 15)).pack()

    root.mainloop()

def login():
    loginWin.destroy()
    Label(root, text='', width='400', height='5', bg=('#2A3D45')).pack()
    Label(root, text='Logged', width='400', height='2', relief='flat', borderwidth='0', bg='#446633', fg='white', font=('Arial', 15)).pack()


def loginScreen():
    global loginWin, userEmail, userPwd, enterEmail, enterPwd

    userEmail = StringVar()
    userPwd = StringVar()

    loginWin = Toplevel(root)
    loginWin.title('Codechat')
    loginWin.configure(background='#2A3D45')
    loginWin.iconbitmap('codechat.png')
    loginWin.geometry('400x400+500+100')
    loginWin.resizable(False, False)
    loginWin.wm_attributes('-alpha', 1)

    Label(loginWin, text='', width='400', bg='#2A3D45', height='2', ).pack()
    Label(loginWin, text='Codechat', width='400', bg='#2A3D45', fg='white', height='1', font=('Arial', 30)).pack()
    Label(loginWin, text='Manage Your Account', bg='#2A3D45', fg='white', width='400', height='1', font=('Arial', 10)).pack()
    Label(loginWin, text='', width='400', bg='#2A3D45', height='2').pack()

    Label(loginWin, text='E-Mail', fg='white', width='400', bg='#2A3D45', height='1').pack()
    enterEmail = Entry(loginWin, bd=0, relief='solid', bg='black', fg='white', text='E-Mail',  borderwidth='0',  width='20', justify='center',  textvariable='userEmail' )
    enterEmail.pack()

    Label(loginWin, text='', width='400', bg='#2A3D45', height='1').pack()

    Label(loginWin,fg='white', text='Password', width='400', bg='#2A3D45', height='1').pack()
    enterPwd = Entry(loginWin, bd=0, relief='solid', bg='black', fg='white', borderwidth='0', text='Password', width='20', justify='center',  textvariable='userPwd')
    enterPwd.config(show='*')
    enterPwd.pack()

    Label(loginWin, text='', width='400', height='2', bg='#2A3D45').pack()
    Button(loginWin, text='Login', bd=80, width='10', command=login).pack()



