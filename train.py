from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkinter import Tk, messagebox
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        title_lbl=Label(self.root,text="TRAIN DATASET",font=("times new roman",35,"bold"),bg="white",fg="maroon")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top = Image.open(r"c:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\FR-Scan-Featured-01-scaled.jpeg")
        img_top = img_top.resize((1530,325))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)
        
        #button
        b1_1=Button(self.root,text="TRAIN DATA",cursor="hand2", command=self.train_classifier, font=("times new roman",30,"bold"),bg="white",fg="black")
        b1_1.place(x=0,y=380,width=1530,height=60)
        
        
        img_bottom = Image.open(r"c:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\faces_landmarks.png")
        img_bottom = img_bottom.resize((1530,325))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)
        
    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir) ] #list comprehensing
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') #grayscaleimage
            imageNp=np.array(img,'uint8') #convert images into grid uint8 is datatype
            id=int(os.path.split(image)[1].split('.')[1])
            
            #C:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition\Data\Users.1.1.jpg
            #0                                                                 1
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow('Training',imageNp)
            # Wait for a key press
            key = cv2.waitKey(1)

    # Check if the Enter key (key code 13) is pressed
            if key == 13:
                break
            
        ids=np.array(ids)
        
        #train class_ifier and save
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.train(faces,ids)
        self.recognizer.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!")
        
        
def main():
    root = Tk()
    app = Train(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()