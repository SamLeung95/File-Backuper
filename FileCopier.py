from tkinter import *
from tkinter import filedialog
import ntpath
import os
import shutil

#Variables

dirName1=""
dirID = {} #Dictionary of button to label
dirMap = {}#Dictionary of button to file path
dirArray = [] #List of currently added buttons
dirAmt = 0 #How many buttons stored

def getDirName():
    global dirName1
    dirName1 = filedialog.askdirectory()
    DirGetPathLabel.configure(text=dirName1)


def getDirName2():
    global dirName1
    dirName1 = filedialog.askopenfilename()
    DirGetPathLabel.configure(text=dirName1)


def getSaveDirName(event):
    
    dirMap[event.widget] = filedialog.askdirectory()
    dirID[event.widget].configure(text=dirMap[event.widget])

def strToStringVar(name):
    temp = StringVar()
    temp.set(name)
    return temp

def AddDir():
    global dirAmt
    global dirID

    
    b = Button(mainFrame, text = "Directory" + str(dirAmt))
    dirMap[b] = ""
    b.bind("<Button-1>", getSaveDirName)
    b.place(x=10,y=(100+(60*dirAmt)))
    
    dirArray.append(b)
    
    l = Label(mainFrame, text = dirMap[b])
    l.place(x=10,y=(130+(60*dirAmt)))
    dirID[b] = l;
    dirAmt = dirAmt + 1

def AddDir2(path):
    global dirAmt
    global dirID
    global dirMap
    global dirArray
    
    b = Button(mainFrame, text = "Directory" + str(dirAmt))
    dirMap[b] = path
    b.bind("<Button-1>", getSaveDirName)
    b.place(x=10,y=(100+(60*dirAmt)))
    
    dirArray.append(b)
    
    l = Label(mainFrame, text = dirMap[b])
    l.place(x=10,y=(130+(60*dirAmt)))
    dirID[b] = l;
    dirAmt = dirAmt + 1

def save():
    print (dirName1)
    for i in range (0,dirAmt):
        print (dirMap[dirArray[i]])
        try:
            num = 0
            tempName = ntpath.basename(str(dirName1)) + str(num)
       
            same = False

            #First check to see if files collide

            if os.path.exists(dirMap[dirArray[i]] + "/" + ntpath.basename(str(dirName1))):
                same = True

            shutil.copy(str(dirName1), dirMap[dirArray[i]])
            
            while same:
                if os.path.exists(dirMap[dirArray[i]] + "/" + tempName):
                    num = num + 1
                    tempName = ntpath.basename(str(dirName1)) + str(num)
                else:
                    shutil.copy(str(dirName1), dirMap[dirArray[i]] + "/" + tempName)
                    same = False
            
        except FileNotFoundError:
            print ("A file or directory was not found.")

def load():
    global dirName1
    global dirAmt
    global dirID
    global dirMap
    global dirArray

    #Clears old buttons and labels
    for i in range (0,dirAmt):
        dirID[dirArray[i]].destroy()
        dirArray[i].destroy()
    dirAmt = 0
    dirMap = {}
    dirID = {}
    dirArray = []

    #Opens files and reads
    text_file = open("Settings.txt", "r")
    file =  text_file.read().splitlines() 
    dirName1 = file[0]
    DirGetPathLabel.configure(text=dirName1)
    for i in range (1,len(file)):
        AddDir2(file[i])
        
    text_file.close()
    
def saveSettings():
    text_file = open("Settings.txt", "w")
    text_file.write(dirName1)
    for i in range (0,dirAmt):

        text_file.write("\n" + dirMap[dirArray[i]])
    text_file.close()

root=Tk()
root.title("File Copier")

mainFrame = Frame(root, width = 600, height = 500)
mainFrame.pack()






#GUI
GetDirLabel = Label(mainFrame, text="Directory to copy:")

GetDirButton = Button(mainFrame, text = "Select Directory", command = getDirName)#Button for choosing directory

GetDirButton2 = Button(mainFrame, text = "Select File", command = getDirName2)

SaveSettingButton = Button(mainFrame, text = "Save Settings", command = saveSettings)#Button for saving settings

LoadSettingButton = Button(mainFrame, text = "Load Settings", command = load)#Button for loading settings

DirGetPathLabel = Label(mainFrame, text=dirName1)#Label for chosen directory

SaveToLabel = Label(mainFrame, text="Directories to copy to:")


AddDirbtnButton = Button(mainFrame, text = "Add more directories", command = AddDir)#Button for Adding directory

SaveButton = Button(mainFrame, text = "Save", command = save)



GetDirLabel.place(x = 0, y = 10)
GetDirButton.place(x = 100, y=8)
GetDirButton2.place(x = 200, y=8)
SaveSettingButton.place(x = 300, y=8)
LoadSettingButton.place(x = 390, y=8)

DirGetPathLabel.place(x = 5, y = 45)

SaveToLabel.place(x = 0, y = 70)
AddDirbtnButton.place(x = 130, y = 68)
               
SaveButton.place(x = 300, y = 68)
root.mainloop()
