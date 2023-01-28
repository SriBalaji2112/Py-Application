from tkinter import *
from tkinter import messagebox
import main

def signUpPage():
    signRoot = Tk()
    signRoot.title("SIGNUP TO CONTINUE")
    signRoot.geometry('925x500+300+200')
    signRoot.configure(bg="#fff")
    signRoot.resizable(False, False)

    def signIn():
        username = user.get()
        password = code.get()

        if username == 'admin' and password == '2112':
            signRoot.destroy()
            print("Success")
            main.mainPage()


        else:
            messagebox.showerror("Invalid", "invalid username or password")

    signUpImg = PhotoImage(file='images/signUp.png')

    imgLabel = Label(signRoot, image=signUpImg, bg='white')
    imgLabel.place(x=50, y=50)

    frame = Frame(signRoot, width=350, height=350, bg='white')
    frame.place(x=480, y=70)

    heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('Microsoft VaHei UI Light', 23, 'bold'))
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
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    ############################################################################

    Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signIn).place(x=35,
                                                                                                              y=204)
    label = Label(frame, text="Already have an account?", fg='black', bg='white',
                  font=('Microsoft VaHei UI Light', 9))
    label.place(x=75, y=270)

    def singInToggel():
        signRoot.destroy()
        main.signInPage()

    signUp = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=singInToggel)
    signUp.place(x=215, y=270)
    signRoot.mainloop()
