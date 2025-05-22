from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("face Recognition System")
        
      title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="brown")
      title_lbl.place(x=0,y=0,width=1530,height=45)
       
      img_top=Image.open(r"C:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\5113470.jpg")
      img_top=img_top.resize((1530,720))
      self.photoimg_top=ImageTk.PhotoImage(img_top)
       
      f_lbl=Label(self.root,image=self.photoimg_top)
      f_lbl.place(x=0,y=55,width=1530,height=720)
       
      dev_label=Label(f_lbl,text="EMAIL:pranjalidalwai@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="white")
      dev_label.place(x=390,y=620)

       
  # add commands in button on main.py for help desk (video time 18.20)
  
  
  
  # exit icon 
  

         
  # add commands in button on main.py for exit (video time 21.09)
  
  
  # current time
  
  #left side of title

         

    
if __name__ == "__main__":
  root=Tk()
  obj=Help(root)
  root.mainloop() 
  
       