from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkinter import Tk, messagebox
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #variables
        self.var_atten_ID=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dept=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        img = Image.open(r"c:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\5118239.jpg")
        img = img.resize((800,200))
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)
        
        #second image
        img1 = Image.open(r"C:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\facial-recognition-connected-real-estate.png")
        img1 = img1.resize((800,200))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)
        
        #bg imge
        img3=Image.open(r"C:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\face-recognition-ar-hologram-screen-smart-technology_53876-167350.jpg")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="ATTENDANCE  SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)
         
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student attendance details",font=("times new roman",13,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)
        
        img_left = Image.open(r"C:\Users\Parshuram  Dalwai\OneDrive\Desktop\Face recognition - Copy\images\images (1)1.jpeg")
        img_left = img.resize((720,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)
        
        attendenceId_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",13,"bold"),bg="white")
        attendenceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendence_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_ID,font=("times new roman",13,"bold"))
        attendence_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        # name
        
        rollLabel=Label(left_inside_frame,text="Roll:",font=("times new roman",13,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)
        
        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        atten_roll.grid(row=0,column=3,pady=8)
        
        # date
        nameLabel=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        nameLabel.grid(row=1,column=0)
        
        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        atten_name.grid(row=1,column=1,pady=8)
        
        #department
        depLabel=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        depLabel.grid(row=1,column=2)
        
        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dept,font=("times new roman",13,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)
        
        #time
        timeLabel=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        timeLabel.grid(row=2,column=0)
        
        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        atten_time.grid(row=2,column=1,pady=8)
        
        #date
        dateLabel=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        dateLabel.grid(row=2,column=2)
        
        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        atten_date.grid(row=2,column=3,pady=8)
        
        #attendence
        attendenceLabel=Label(left_inside_frame,text="Attendence Status:",font=("times new roman",13,"bold"),bg="white")
        attendenceLabel.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=22,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",13,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=500)
         
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455) 
         
        #scrollbar
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)
        
        self.AttendenceReportTable.heading("id",text="Attendance ID")  
        self.AttendenceReportTable.heading("roll",text="Roll")  
        self.AttendenceReportTable.heading("name",text="Name")  
        self.AttendenceReportTable.heading("department",text="Department") 
        self.AttendenceReportTable.heading("time",text="Time")  
        self.AttendenceReportTable.heading("date",text="Date")  
        self.AttendenceReportTable.heading("attendance",text="Attendance")   
        
        self.AttendenceReportTable["show"]="headings"
        
        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendance",width=100)
        
        
         
        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        #fetch data
    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)
    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)
        
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found To Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data Exported to " + os.path.basename(fln) + " Successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
            
    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_ID.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dept.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
    
    def reset_data(self):
        self.var_atten_ID.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dept.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
            
    
def main():
    root = Tk()
    app = Attendance(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()