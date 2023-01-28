# https://github.com/SriBalaji2112
# Login & SignUp GUI
# 28/01/2023

from tkinter import *
from tkinter import messagebox
import signUpPage

### Main Page UI

def mainPage():
    mainRoot = Tk()
    mainRoot.title("App")
    mainRoot.geometry('925x500+300+200')
    mainRoot.config(bg="white")

    Label(mainRoot, text='Hello Everyone!', bg="#fff", font=('Calibri(body)', 50, 'bold')).pack(expand=True)
    mainRoot.mainloop()

### signUppage

# def signUpPage():
#
# ### Sign In Page UI

def signInPage():
    root = Tk()
    root.title("LOGIN TO CONTINUE")
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False, False)

    def signIn():
        username = user.get()
        password = code.get()

        # In this place you will add your DB

        if username == 'admin' and password == '2112':    # Check ID && Password
            root.destroy()
            print("Success")
            mainPage()


        else:
            messagebox.showerror("Invalid", "invalid username or password")


    loginImg = PhotoImage(file='images/signIn.png')

    Label(root, image=loginImg, bg='white').place(x=50, y=50)

    frame = Frame(root, width=350, height=350, bg='white')
    frame.place(x=480, y=70)

    heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft VaHei UI Light', 23, 'bold'))
    heading.place(x=110, y=5)

    #################----------------------------------------------------------------------------------------------

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft VaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    #################-----------------------------------------------------------------------------------------------
    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, 'Password')

    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft VaHei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind('<Return>', signIn)
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)


    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    ############################################################################

    Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signIn).place(x=35,
                                                                                                              y=204)
    label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft VaHei UI Light', 9))
    label.place(x=75, y=270)

    def signPageToggel():
        root.destroy()
        signUpPage.signUpPage()

    signUp = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signPageToggel)
    signUp.place(x=215, y=270)
    root.mainloop()


if __name__ == '__main__':
    signInPage()