# TKinter SB_Notepad
# https://github.com/SriBalaji2112
# 29/01/2023


from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from customtkinter import *
set_appearance_mode("default")
set_default_color_theme("blue")


class Notepad:
    root = CTk()

    # default window width and height
    winWidth = 300
    winHeight = 300
    font = CTkFont(size=23, family='TimeNewRoman')
    textArea = Text(root, font=font)
    menuBar = Menu(root, font=font)
    fileMenu = Menu(menuBar, tearoff=0)
    editMenu = Menu(menuBar, tearoff=0)
    helpMenu = Menu(menuBar, tearoff=0)

    # To add scrollbar
    scrollBar = Scrollbar(textArea)
    __file = None

    def __init__(self, **kwargs):

        # Set icon
        try:
            self.root.wm_iconbitmap("python.png")
        except:
            pass

        # Set window size (the default is 300x300)

        try:
            self.winWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.winHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.root.title("Untitled - SB_Notepad")

        # Center the window
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        # For left-align
        left = (screenWidth / 2) - (self.winWidth / 2)

        # For right-align
        top = (screenHeight / 2) - (self.winHeight / 2)

        # For top and bottom
        self.root.geometry('%dx%d+%d+%d' % (self.winWidth,
                                              self.winHeight,
                                              left, top))

        # To make the textarea auto resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.textArea.grid(sticky=N + E + S + W)

        # To open new file
        self.fileMenu.add_command(label="New",
                                        command=self.__newFile)

        self.fileMenu.add_command(label="New Window", command=self.newWin)

        # To open a already existing file
        self.fileMenu.add_command(label="Open",
                                        command=self.__openFile)

        # To save current file
        self.fileMenu.add_command(label="Save",
                                        command=self.__saveFile)

        self.fileMenu.add_command(label="Save As", command=self.__saveAsFile)

        # To create a line in the dialog
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.menuBar.add_cascade(label="File",
                                       menu=self.fileMenu)

        # To give a feature of cut
        self.editMenu.add_command(label="Cut",
                                        command=self.__cut)

        # to give a feature of copy
        self.editMenu.add_command(label="Copy",
                                        command=self.__copy)

        # To give a feature of paste
        self.editMenu.add_command(label="Paste",
                                        command=self.__paste)

        # To give a feature of editing
        self.menuBar.add_cascade(label="Edit",
                                       menu=self.editMenu)

        # To create a feature of description of the notepad
        self.helpMenu.add_command(label="About Notepad",
                                        command=self.__showAbout)
        self.menuBar.add_cascade(label="Help",
                                       menu=self.helpMenu)

        self.root.config(menu=self.menuBar)

        self.scrollBar.pack(side=RIGHT, fill=Y)

        self.scrollBar.config(command=self.textArea.yview)
        self.textArea.config(yscrollcommand=self.scrollBar.set)

    def __quitApplication(self):
        self.root.destroy()

    # exit()

    def newWin(self):
        showinfo("Sorry - SB_Notepad", "Open New Window Option will update soon...")

    def __showAbout(self):
        showinfo("About - SB_Notepad", "Balaji Santhanam\ncontact : https://github.com/SriBalaji2112/Py-Apllication")

    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.__file == "":

            # no file to open
            self.__file = None
        else:

            # Try to open the file
            # set the window title
            self.root.title(os.path.basename(self.__file) + " - Notepad")
            self.textArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.textArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.root.title("Untitled - SB_Notepad")
        self.__file = None
        self.textArea.delete(1.0, END)

    def __saveAsFile(self):
        self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])
        if self.__file == "":
            self.__file = None
        else:

            # Try to save the file
            file = open(self.__file, "w")
            file.write(self.textArea.get(1.0, END))
            file.close()

            # Change the window title
            self.root.title(os.path.basename(self.__file) + " - Notepad")


    def __saveFile(self):

        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:

                # Try to save the file
                file = open(self.__file, "w")
                file.write(self.textArea.get(1.0, END))
                file.close()

                # Change the window title
                self.root.title(os.path.basename(self.__file) + " - SB_Notepad")


        else:
            file = open(self.__file, "w")
            file.write(self.textArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.textArea.event_generate("<<Cut>>")

    def __copy(self):
        self.textArea.event_generate("<<Copy>>")

    def __paste(self):
        self.textArea.event_generate("<<Paste>>")

    def run(self):

        # Run main application
        self.root.mainloop()


# Run main application
notepad = Notepad(width=1000, height=600)
notepad.run()
