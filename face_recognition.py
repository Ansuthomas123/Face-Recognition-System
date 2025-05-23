from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkinter import Tk, messagebox
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="FACE RECOGNIZER",font=("times new roman",35,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top = Image.open(r"C:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\facial-recognition-connected-real-estate.png")
        img_top = img_top.resize((650,700))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)
        
        img_bottom = Image.open(r"C:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\800_390_face-recognition.png")
        img_bottom = img_bottom.resize((950,700))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)
        
        b1_1=Button(f_lbl,text="FACE DETECTOR",cursor="hand2",command=self.face_recog, font=("times new roman",18,"bold"),bg="white",fg="black")
        b1_1.place(x=535,y=620,width=200,height=40)
    #attendance
    def mark_attendance(self,i,r,n,d):
            with open("C:\\Users\\Parshuram  Dalwai\\OneDrive\\Desktop\\Face recognition - Copy\\pranjali.csv", "r+" ,newline="\n") as f:
                myDataList=f. readlines()
                name_list=[]
                for line in myDataList:
                    entry=line.split((","))
                    name_list.append(entry[0])
                if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
    
    #facerecognition
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="root1234",database="face_recognizer")
                my_cursor=conn.cursor()
                
                my_cursor.execute("Select Name, Roll, Dept FROM student WHERE Student_id=" + str(id))
                result = my_cursor.fetchone()
                n, r, d = result if result else ("Unknown", "Unknown", "Unknown")
                i = str(id) if id else "Unknown"
                
                '''my_cursor.execute("Select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("Select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("Select Dept from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                my_cursor.execute("Select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)'''
                
                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,y]
                
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("C:\\Users\\Parshuram  Dalwai\\OneDrive\\Desktop\\Face recognition - Copy\\haarcascade_frontalface_default.xml") 
        recognizer =cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("C:\\Users\\Parshuram  Dalwai\\OneDrive\\Desktop\\Face recognition - Copy\\Classifier.xml") 
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,recognizer,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
                
            key = cv2.waitKey(1)
            if key == 27:
                break
        video_cap.release()
        cv2.destroyAllWindows()
                 
def main():
    root = Tk()
    app = Face_Recognition(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()