from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from face_recognition import Face_Recognition
from train import Train
from attendance import Attendance
from helpdesk import Help
import tkinter
from time import strftime
from datetime import datetime

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        img = Image.open(r"c:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\ig1.jpg")
        img = img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        img1 = Image.open(r"C:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\ig3.jpg")
        img1 = img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        img2 = Image.open(r"C:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\ig4.jpg")
        img2 = img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
        
        img3=Image.open(r"C:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\ig2.jpg")
        img3=img3.resize((1500,800))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE  SYSTEM ",font=("times new roman",30,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
    

        lbl = Label(title_lbl, font =('times new roman',14,'bold'),background = 'white', foreground = 'blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        
        img4 = Image.open(r"c:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\WhatsApp Image 2023-10-02 at 22.25.36.jpg")
        img4 = img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)        
        
        b1_1=Button(bg_img,text="STUDENT DETAIL",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=300,width=220,height=40)

       
        img5 = Image.open(r"c:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\WhatsApp Image 2023-10-02 at 22.25.389.jpg")
        img5 = img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.attendance)
        b1.place(x=500,y=100,width=220,height=220)        
        
        b1_1=Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attendance,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=500,y=300,width=220,height=40)


        img6 = Image.open(r"C:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\WhatsApp Image 2023-10-02 at 22.25.378.jpg")
        img6 = img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=800,y=100,width=220,height=220)        
        
        b1_1=Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        
        img7 = Image.open(r"c:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\360_F_158216984_zSFxdd273rSrPmwnsK1mwukR5c2N0zWq.jpg")
        img7 = img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help)
        b1.place(x=1100,y=100,width=220,height=220)        
        
        b1_1=Button(bg_img,text="HELP DESK",cursor="hand2",command=self.help,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        
        img8 = Image.open(r"c:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\WhatsApp Image 2023-10-02 at 22.23.375.jpg")
        img8 = img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)        
        
        b1_1=Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=580,width=220,height=40)
        
        
        img10 = Image.open(r"c:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\WhatsApp Image 2023-10-02 at 22.23.363.jpg")
        img10 = img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)        
        
        b1_1=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=500,y=580,width=220,height=40)
        
        
        img11 = Image.open(r"C:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\WhatsApp Image 2023-10-02 at 22.23.352.jpg")
        img11 = img11.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=800,y=380,width=220,height=220)        
        
        b1_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=800,y=580,width=220,height=40)
    
    
    def open_img(self):
        os.startfile("Data")
        
    def iExit(self):
      self.iExit=tkinter.messagebox.askyesno("Face Recognition","You sure to exit this window",parent=self.root)
      if self.iExit>0:
        self.root.destroy()
      else:
        return    
        
        
        #function button
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
            
if __name__=="__main__":
    root=Tk()
    obj=FaceRecognitionSystem(root)
    root.mainloop()

    
            