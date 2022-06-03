# import libraries of GUI(Graphical User Interface)
from tkinter import*
from tkinter.messagebox import showinfo   # this modul(messagebox) is used to display message using provide number of functions. 
from tkinter.filedialog import Open,askopenfilename,asksaveasfilename   # import only asksaveasfile from filedialog which is used to save file in any extension
import os    #os.path, module include many fuctions to interact with the file system
from setuptools import command # using setuptools for distribution as it has greater functionality.

# Start function command

def NewFile():
    global file
    root.title("Untitled - Notepad") # create a title name on the titlebar
    file=None
    TextArea.delete(1.0,END) # delete first line and zero column to End

def OpenFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + "- Notepad") # try to open the file
                                                         # set the window title
        TextArea.delete(1.0,END)
        f=open(file,"r")  #"r": open file in read-only mode.
        TextArea.insert(1.0, f.read())
        f.close()

def SaveFile():
    global file
    if file==None:
        #function to call when user press the save button,a filedialog will open and ask to save file.
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.text")])
        if file=="": #not selected any file then  file=None
            file=None
        else:
            # Save as a new file
            f=open(file,"w") #"w": Open file in write-only mode.
            f.write(TextArea.get(1.0,END))
            f.close()
            
            root.title(os.path.basename(file)+ "- Notepad")
            print("File Saved")
    else:
        # Save the file
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
            

def quitApp():
    root.destroy()

def Cut():
    TextArea.event_generate(("<<Cut>>"))

def Copy():
    TextArea.event_generate(("<<Copy>>"))

def Paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by Akash kumar")

  

if __name__ == '__main__':
   #Basic tkinter setup
   root=Tk()
   root.title("Untitled - Notepad") #create a title Name
   root.wm_iconbitmap("images.png") #wm_iconbitmap are used for set icon on titlebar.only used for png images.
   root.geometry("644x788")
   
   #Add TextArea
   TextArea = Text(root,font="lucida 13")
   file=None
   TextArea.pack(expand=True,fill=BOTH) #fill=BOTH are use for resize window x-axis and y-axis.
   
   #Lets create a Menubar
   MenuBar=Menu(root)
   FileMenu=Menu(MenuBar,tearoff=0) # tearoff is used to remove dotted line 
   
   #To open new file
   FileMenu.add_command(label="New",command=NewFile)
   
   #To open already existing file
   FileMenu.add_command(label="Open",command=OpenFile)
   
   #To save the current file
   FileMenu.add_command(label="Save",command=SaveFile)
   FileMenu.add_separator() # add_separator is used for create divider line between Menu.
   FileMenu.add_command(label="Exit",command=quitApp)
   MenuBar.add_cascade(label="File",menu=FileMenu)
   # End File Menue
   
   
   #Edit Menu Starts
   EditMenu = Menu(MenuBar,tearoff=0)
   
   #Create a features of cut,copy and paste.
   EditMenu.add_command(label="Cut",command=Cut)
   EditMenu.add_command(label="Copy",command=Copy)
   EditMenu.add_command(label="Paste",command=Paste)
   
   MenuBar.add_cascade(label="Edit",menu=EditMenu)
   # End Edit Menu
   
   # Help Menu Starts
   HelpMenu=Menu(MenuBar,tearoff=0)
   HelpMenu.add_command(label="About Notepad",command=about)
   MenuBar.add_cascade(label="Help",menu=HelpMenu)
   
   #End Help Menu
   
   
   
   
   
   
   root.config(menu=MenuBar)   # tkinter config() function,used to simply change the text on a label.
   
   # Adding Scrollbar 
   Scroll=Scrollbar(TextArea)
   Scroll.pack(side=RIGHT,fill=Y) # Create Scrollbar of Notepad window on write side
   Scroll.config(command=TextArea.yview)
   TextArea.config(yscrollcommand=Scroll.set)   
   
   
   
   
   
   
   root.mainloop()
   