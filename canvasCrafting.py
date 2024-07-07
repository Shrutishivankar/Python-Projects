from tkinter import*
from tkinter import Toplevel,Button
from tkinter import colorchooser
import PIL.ImageGrab as ImageGrab
from tkinter import filedialog,messagebox

##_____TEXT-EDITOR____

def open_text_editor():
    text_window = Toplevel(r)
    text_window.title("Text_editor")
    text_window.geometry("1100x600")
    text_window.maxsize(1100,600)
    text_window.minsize(1100,600)

    def newFile():
        text.delete(1.0 , END)

    def openFile():
        filepath = filedialog.askopenfilename(defaultextension =".txt" , filetypes =[("Text files" , "*.txt")],parent=text_window)  
        # if filepath is not open then with open statement open the file in read mode and insert their context in textbox
        if filepath:
            with open (filepath , 'r') as file:
                text.delete(1.0 , END)
                text.insert(END , file.read())

    def saveAsFile():
        filepath = filedialog.asksaveasfilename(defaultextension =".txt" , filetypes =[("Text files","*.txt")],parent=text_window)
        if filepath:
            with open (filepath ,'w') as file:
                file.write(text.get(1.0 , END))
                messagebox.showinfo("Info" , "File Saved Successfully!!")

    def exitFile():
        if messagebox.askyesno("Text-Editor","are you sure you want to exit?",parent=text_window):
            text_window.destroy()         

    ## _1.FILE MENU_
     #add file menu into menu widget using cascade method  
    #set menu widget in text_window(i.e. root/location) using config method          
    
    menuBar = Menu(text_window)
    text_window.config(menu=menuBar)
    fileMenu = Menu(menuBar)
    menuBar.add_cascade(label="File" ,menu=fileMenu)
    fileMenu.add_command(label="New" , command=newFile)
    fileMenu.add_command(label="Open" , command=openFile)
    fileMenu.add_command(label="SaveAs" , command=saveAsFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit" , command=exitFile)

## _2.EDIT MENU_
    
    '''
        1.text: This refers to the Text widget where the user is working or typing text.
        2.event_generate(): This is a method of the Text widget that generates an event and triggers the associated action.
        3."<<Cut>>": Triggers the "Cut" action, which cuts the selected text and places it in the clipboard.
    '''
    def cutText():
        text.event_generate("<<Cut>>")    
    def copyText():
        text.event_generate("<<Copy>>")    
    def pasteText():
        text.event_generate("<<Paste>>") 

    #Tkinter itself doesn't provide built-in undo and redo functionality; you have to implement it manually.       
    editMenu = Menu(menuBar) 
    menuBar.add_cascade(label="Edit" ,menu=editMenu)
    editMenu.add_command(label="Cut" ,command=cutText)
    editMenu.add_command(label="Copy" ,command=copyText)
    editMenu.add_command(label="Paste" ,command=pasteText)

## _3. TEXT-FRAME _

# variable for text is textValue of string type
    '''textValue=StringVar()
    def writeText(event):
         text.create_text(event.x,event.y ,text= textValue.get()) '''
    
    f1_txt = Frame(text_window,height=10,width=400)
    f1_txt.grid(row=0 , column=0)
    textFrame = Frame(f1_txt,height=10,width=400,relief=SUNKEN,borderwidth=3)
    textFrame.grid(row=0 , column=5)

    textLabel = Label(textFrame,text="Write your Note / Text here....",width=155,bg="white")
    textLabel.grid(row=0 , column=0)

    '''textAreaEntry = Entry(textFrame,textvariable=textValue,width=180,bg="white")         # EntryWidget
    textAreaEntry.grid(row=1 , column=0) '''
    def clearText():
            text.delete(1.0 , END) 

    clearTextButton = Button(textFrame,text="Clear",width=155,bg="white",command=clearText)    
    clearTextButton.grid(row=2 , column=0)
    
    ##_____TEXT-WIDGET____

    f2_txt = Frame(text_window,height=300,width=1100,bg="black")
    f2_txt.grid(row=1 , column=0)

    text = Text(f2_txt , wrap=WORD , font=("Helvetica",14) ,fg="black")
    text.pack(expand=YES , fill=BOTH)
    #Wrap parameter: wraps the text into Word boundary(The written text is not go out of boundary so wrapping is necessary)
    #text.bind("<Button-1>",writeText)
    
    text_window.mainloop()

##________PAINT-APPLICATION_________
    
#In your code, prevPoint is defined inside the paint function, but you're trying to use it outside that function.   
#To resolve this issue prevPoint and currentPoint are defined outside the functions as global variables, so they can be accessed and modified from within the paint function as well as other parts of the code.     

## Variables for pencil
prevPoint =[0,0]
currentPoint =[0,0]

def open_paint_app():
    global prevPoint, currentPoint
    root = Toplevel(r)
    root.title("Paint_Application")
    root.geometry("1100x600")
    root.maxsize(1100,600)
    root.minsize(1100,600)

    ## ___FRAME-1 : INTERFACE___
    frame1 = Frame(root,height=100,width=1100)
    frame1.grid(row=0 , column=0 , sticky=NW)

    ## ____1.TOOLS FRAME____
    toolsFrame = Frame(frame1,height=100,width=100,relief=SUNKEN,borderwidth=3)
    toolsFrame.grid(row=0 , column=0)

    def usePencil():
        stroke_color.set("black")
        canvas["cursor"] = "arrow"

    def useEraser():
        stroke_color.set("white")
        canvas["cursor"] = "dotbox"

    pencilButton = Button(toolsFrame,text="Pencil",width=11,command=usePencil)    
    pencilButton.grid(row=0 , column=0)

    eraserButton = Button(toolsFrame,text="Eraser",width=11,command=useEraser)    
    eraserButton.grid(row=1 , column=0)  

    toolsLabel = Label(toolsFrame,text="Label",width=11)
    toolsLabel.grid(row=2 , column=0)

    ## ____2.DROPDOWN LIST(SIZE-FRAME)___

    sizeFrame = Frame(frame1,height=100,width=100,relief="sunken",borderwidth=3)
    sizeFrame.grid(row=0 , column=1)

    defaultButton = Button(sizeFrame,text="Default",width=10,command=usePencil)
    defaultButton.grid(row=0 , column=0)

    stroke_size =IntVar()
    stroke_size.set(1)            # By default value of pencil size

    options =[1,2,3,4,5,6,7,8,9,10]

    sizeList = OptionMenu(sizeFrame,stroke_size, *options)
    sizeList.grid(row=1 , column=0)

    sizeLabel =Label(sizeFrame,text="Size",width=10)
    sizeLabel.grid(row=2 ,column=0)

    ## ______3.COLORBOX-FRAME________
    colorBoxFrame = Frame(frame1,height=100,width=100,relief="sunken",borderwidth=3)
    colorBoxFrame.grid(row=0 , column=2)

    def selectColor():
        selectedColor = colorchooser.askcolor("red",parent=root)       #parent=root is for holding the selectColor() nor to hide behind other window
        print(selectedColor)
        if selectedColor == None :
            stroke_color.set("black")
        else : 
            stroke_color.set(selectedColor[1])       
            # Somehow it showing tuple for e.g like this :((255,0,0),'#ff000')
            # So, we mention array index as [1] for selectedColor
            
    colorBoxButton =Button(colorBoxFrame,text="Select Color",width=40,command=selectColor)
    colorBoxButton.grid(row=0 , column=0)

    ## _____4. COLORS-FRAME (RGB)_____
    colorsFrame = Frame(frame1,height=100,width=100,relief=SUNKEN,borderwidth=3)
    colorsFrame.grid(row=0 , column=3)

    #A lambda function is a small anonymous function that can take any number of arguments and return a result.
    redButton = Button(colorsFrame,text="RED",width=10,bg="red",command=lambda: stroke_color.set("red"),relief=SUNKEN,borderwidth=3)
    redButton.grid(row=0 , column=0)

    greenButton = Button(colorsFrame,text="GREEN",width=10,bg="green",command=lambda: stroke_color.set("green"),relief=SUNKEN,borderwidth=3)
    greenButton.grid(row=1 , column=0)

    blueButton = Button(colorsFrame,text="BLUE",width=10,bg="blue",command=lambda: stroke_color.set("blue"),relief=SUNKEN,borderwidth=3)
    blueButton.grid(row=2 , column=0)

    pinkButton = Button(colorsFrame,text="PINK",width=10,bg="pink",command=lambda: stroke_color.set("pink"),relief=SUNKEN,borderwidth=3)
    pinkButton.grid(row=0 , column=1)

    purpleButton = Button(colorsFrame,text="PURPLE",width=10,bg="purple",command=lambda: stroke_color.set("purple"),relief=SUNKEN,borderwidth=3)
    purpleButton.grid(row=1 , column=1)

    yellowButton = Button(colorsFrame,text="YELLOW",width=10,bg="yellow",command=lambda: stroke_color.set("yellow"),relief=SUNKEN,borderwidth=3)
    yellowButton.grid(row=2 , column=1)

    ## __________5. SAVEIMAGE-FRAME____________

    def saveImage():
        filelocation = filedialog.asksaveasfilename(defaultextension="jpg",parent=root)
        # we calculate the coordinates and dimensions of the canvas (frame2) relative to the screen using winfo_x(), winfo_y(), winfo_width(), and winfo_height() methods. 
        x = root.winfo_rootx() + frame2.winfo_x()       # x co-ordinate of canvas
        y = root.winfo_rooty() + frame2.winfo_y()       # y co-ordinate of canvas
        width = frame2.winfo_width()                    # width of canvas
        height = frame2.winfo_height()                  # height of canvas

        img = ImageGrab.grab(bbox=(x,y,x+width,y+height))     # (bbox:bounding box)
        img.save(filelocation)
        showImage = messagebox.askyesno("Paint App","Do you want to open image?")
        #print(showImage)
        if showImage:
           img.show()

    def clear():
        if messagebox.askokcancel("Paint App","Do you want to clear everything?",parent=root):
            canvas.delete("all")    

    def createNew():
        if messagebox.askyesno("Paint App","Do you want to save before clear everything?",parent=root):
           clear()
           saveImage()

    saveImageFrame = Frame(frame1,height=100,width=100,relief=SUNKEN,borderwidth=3)
    saveImageFrame.grid(row=0 , column=4)

    saveImgButton = Button(saveImageFrame,text="SAVE",width=10,bg="white",command=saveImage)
    saveImgButton.grid(row=0 , column=0)

    newImgButton = Button(saveImageFrame,text="NEW",width=10,bg="white",command=createNew)
    newImgButton.grid(row=1 , column=0)

    clearImgButton = Button(saveImageFrame,text="CLEAR",width=10,bg="white",command=clear)
    clearImgButton.grid(row=2 , column=0)

    ## __________6. HELP_SETTING-FRAME____________

    def help():
        messagebox.showinfo("Help", "1.Click on Select color option to select custom colors \n 2.Click on Clear to clear entire canvas \n 3.Click on Open option to move to text-editor and close  the paint application.",parent=root)

    def settings():
        messagebox.showwarning("Settings","Not Available yet!!",parent=root)

    def about():
        messagebox.showinfo("About","Ensuring everyone can create creative design with us.. \n This Paint app is best for beginners..",parent=root)   

    helpSettingFrame = Frame(frame1,height=100,width=100,relief="sunken",borderwidth=3)
    helpSettingFrame.grid(row=0 , column=5)

    helpButton = Button(helpSettingFrame,text="HELP",width=10,bg="white",command=help)
    helpButton.grid(row=0 , column=0)

    settingsButton = Button(helpSettingFrame,text="SETTINGS",width=10,bg="white",command=settings)
    settingsButton.grid(row=1 , column=0)

    aboutButton = Button(helpSettingFrame,text="ABOUT",width=10,bg="white",command=about)
    aboutButton.grid(row=2 , column=0)

    ## ___7. TO OPEN SECOND WINDOW/FRAME(TEXTEDITOR) ___

    openingFrame =Frame(frame1,height=100,width=1100,relief=SUNKEN,borderwidth=3)
    openingFrame.grid(row=0 , column=6)

    label = Label(openingFrame, text='Move to Text-Editor',width=38)
    label.grid(row=0,column=0)

    button = Button(openingFrame, text='Open',width=38,command=open_text_editor)
    button.grid(row=1,column=0) 

    ## ______FRAME-2 : CANVAS_____

    frame2 = Frame(root,height=500,width=1100)
    frame2.grid(row=1 , column=0)

    ## Create an Canvas 
    # canvas = Canvas(frame2,height=500,width=1100,bg="white",cursor=DOTBOX)    # if we do not use functions
    canvas = Canvas(frame2,height=500,width=1100,bg="white")
    canvas.grid(row=0 , column=0)
    # canvas.create_line(100,100,200,200)
    # canvas.create_oval(300,300,150,150,fill="black")
    stroke_color =StringVar()
    stroke_color.set("black")      # By default value of pencil

    ## Draw on Canvas using tkinter
    def paint(event):
        # print(event.type)
        global prevPoint
        global currentPoint
        x =event.x
        y = event.y
        currentPoint =[x,y]

        if prevPoint !=[0,0]:
           # canvas.create_oval(x,y,x+5,y+5,fill="black")
           canvas.create_polygon(prevPoint[0],prevPoint[1],currentPoint[0],currentPoint[1],fill=stroke_color.get(),outline=stroke_color.get(),width=stroke_size.get())

        prevPoint = currentPoint

        if event.type == "5":
           prevPoint =[0,0] 

    # canvas.bind("<Button-1>",paint)  
    # for do it in motion we have to use "<B1-motion>"  
    canvas.bind("<B1-Motion>",paint)
    canvas.bind("<ButtonRelease-1>",paint)

    root.mainloop()
    # root.mainloop(): Enters the main event loop, which listens for user interactions and keeps the GUI application running.

r = Tk()
r.title("Canvas Crafting")
r.geometry("1100x600")
r.maxsize(1100,600)
r.minsize(1100,600)

# img_path = PhotoImage(file=r"C:\Users\LENOVO\Downloads\canvas_img (1).png")
img_path = PhotoImage(file=r"C:\Users\LENOVO\Documents\MCAProject_data\canva-img.png")

bgImage = Label(r,image = img_path)
bgImage.place(relheight=1,relwidth=1)

label1 =Label(r,text="Paint Application:",font=("Comic Sans MS", 10),bg="lightgrey")
label1.place(relx=0.4, rely=0.6, anchor='center')
label2 =Label(r,text="Text Editor:",font=("Comic Sans MS", 10),bg="lightgrey")
label2.place(relx=0.4, rely=0.7, anchor='center')

# Create buttons to open new windows
button1 =Button(r , text ="Open",width=8,font=("Comic Sans MS", 8),command=open_paint_app)
button1.place(relx=0.5, rely=0.6, anchor='center')

button2 = Button(r , text ="Open",width=8,font=("Comic Sans MS", 8),command=open_text_editor )
button2.place(relx=0.5, rely=0.7, anchor='center')

r.resizable(False,False)
r.mainloop()