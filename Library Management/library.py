from tkinter import ttk
from tkinter import *
import mysql.connector
from tkinter import messagebox 
import datetime


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1350x750+0+0")


        # =========================VARIABLE=================================
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar
        self.mobile_var = StringVar
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar
        self.auther_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysOnBook = StringVar()
        self.lateratefine_var = StringVar()
        self.dateoverdue = StringVar()
        self.finallprice = StringVar()




        # Title Label
        lbltitle = Label(
            self.root,
            text="Library Management System",
            bg="powder blue",
            fg="green",
            bd=20,
            relief=RIDGE,
            font=("times new roman", 50, "bold"),
            padx=2,
            pady=6,
        )
        lbltitle.pack(side=TOP, fill=X)

        # Main Frame
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1350, height=400)


        # ======================DATA FRAME LEFT======================================
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information",
            bg="powder blue",
            fg="green",
            bd=12,
            relief=RIDGE,
            font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=850, height=350)


        lblMember = Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember = ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman", 12, "bold"),width =20,state="readonly")
        comMember['values'] = ('Admin Staff', 'Student', 'Lecturer')
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblPRN_No = Label(DataFrameLeft,bg="powder blue",text="PRN No:",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.prn_var,width=22)
        txtPRN_No.grid(row=1,column=1,padx=2,pady=6)


        lblTitle = Label(DataFrameLeft,bg="powder blue",text="ID No:",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.id_var,width=22)
        txtTitle.grid(row=2,column=1,padx=2,pady=6)


        lblFirstName = Label(DataFrameLeft,bg="powder blue",text="FirstName",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.firstname_var,width=22)
        txtFirstName.grid(row=3,column=1,padx=2,pady=6)


        lblLastName = Label(DataFrameLeft,bg="powder blue",text="LastName",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.lastname_var,width=22)
        txtLastName.grid(row=4,column=1,padx=2,pady=6)


        lblAddress1 = Label(DataFrameLeft,bg="powder blue",text="Address1",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.address1_var,width=22)
        txtAddress1.grid(row=5,column=1,padx=2,pady=6)


        lblAddress2 = Label(DataFrameLeft,bg="powder blue",text="Address2",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.address2_var,width=22)
        txtAddress2.grid(row=6,column=1,padx=2,pady=6)


        lblPostCode = Label(DataFrameLeft,bg="powder blue",text="Post Code",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.postcode_var,width=22)
        txtPostCode.grid(row=7,column=1,padx=2,pady=6)


        lblMobile = Label(DataFrameLeft,bg="powder blue",text="Mobile",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.mobile_var,width=22)
        txtMobile.grid(row=8,column=1,padx=2,pady=6)


        lblBookId = Label(DataFrameLeft,bg="powder blue",text="Book Id",font=("times new roman", 12, "bold"),padx=2)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.bookid_var,width=22)
        txtBookId.grid(row=0,column=3,padx=2,pady=6)


        lblBookTitle = Label(DataFrameLeft,bg="powder blue",text="Book Title",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.booktitle_var,width=22)
        txtBookTitle.grid(row=1,column=3,padx=2,pady=6)


        lblAuther = Label(DataFrameLeft,bg="powder blue",text="Auther Name",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.auther_var,width=22)
        txtAuther.grid(row=2,column=3,padx=2,pady=6)


        lblDateBorrowed = Label(DataFrameLeft,bg="powder blue",text="Date Borrowed",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.dateborrowed_var,width=22)
        txtDateBorrowed.grid(row=3,column=3,padx=2,pady=6)


        lblDateDue = Label(DataFrameLeft,bg="powder blue",text="Date Due:",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.datedue_var,width=22)
        txtDateDue.grid(row=4,column=3,padx=2,pady=6)


        lblDaysOnBook = Label(DataFrameLeft,bg="powder blue",text="days On Book:",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.daysOnBook,width=22)
        txtDaysOnBook.grid(row=5,column=3,padx=2,pady=6)


        lblLateReturnFine = Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.lateratefine_var,width=22)
        txtLateReturnFine.grid(row=6,column=3,padx=2,pady=6)


        lblDateOverdate = Label(DataFrameLeft,bg="powder blue",text="Date Over Due",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        txtDateOverdate=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.dateoverdue,width=22)
        txtDateOverdate.grid(row=7,column=3,padx=2,pady=6)


        lblActualPrice = Label(DataFrameLeft,bg="powder blue",text="Actual Price",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.finallprice,width=22)
        txtActualPrice.grid(row=8,column=3,padx=2,pady=6)

        # ========================DATA FRAME RIGHT================================
        DataFrameRight = LabelFrame(frame, text="Book Details",
            bg="powder blue",
            fg="green",
            bd=12,
            relief=RIDGE,
            font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=870, y=5, width=400, height=350)


        self.txtBox=Text(DataFrameRight,font=("times new roman", 12, "bold"),width=25,height=15,padx=4,pady=6)
        self.txtBox.grid(row=0,column=2)
         
        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")
        
        listbooks=['Head first book','Learn Python the Hard Way','Python Programming','Secret Rahshy','Python Codebook','Into to Machine Learning','Machine Techo','My Python','Joss Elif Guru','Elite Jungle Python','Jungli Python','Machine Python','Advanced Python','Inton Python','RedChili Python','Ishq Python']


        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection))
            x=value
            if (x=="Head First Book"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Paul Berry")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysOnBook.set(15)
                self.lateratefine_var("Rs.50")
                self.dateoverdue.set("No")
                self.finallprice.set("Rs.788")

        listBox = Listbox(DataFrameRight,font=("times new roman", 12, "bold"),width=15,height=15)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4,pady=6)
        listScrollbar.config(command=listBox.yview)

        



        # ===========================================================================================
        for item in listbooks:
            listBox.insert(END, item)
        # ==============================BUTTONS FRAME==================================

        FrameButton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameButton.place(x=0, y=530, width=1350, height=70)

        btnAddData = Button(FrameButton,command=self.adda_data,text="Add Data",font=("times new roman", 12, "bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0,padx=10,pady=10)

        btnAddData = Button(FrameButton,text="Show Data",font=("times new roman", 12, "bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1,padx=10,pady=10)

        btnAddData = Button(FrameButton,text="Update",font=("times new roman", 12, "bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2,padx=10,pady=10)

        btnAddData = Button(FrameButton,text="Delete",font=("times new roman", 12, "bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3,padx=10,pady=10)

        btnAddData = Button(FrameButton,text="Reset",font=("times new roman", 12, "bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4,padx=10,pady=10)

        btnAddData = Button(FrameButton,text="Exit",font=("times new roman", 12, "bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5,padx=10,pady=10)
        
    # =============================INFORMATION FRAME==================================

        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=600, width=1350, height=95)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1200, height=80)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_frame,columns=("membertype","prnno","title","firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","auther","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)


        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="DateOverdue")
        self.library_table.heading("finalprice",text="Final Price")


        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username = "root",password="test@123",database = "Mydata")
        my_cursor = conn.cursor()

        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)"(
                self.member_var.get(),
                self.prn_var.get(),
                self.id_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.address1_var.get(),
                self.address2_var.get(),
                self.postcode_var.get(),
                self.mobile_var.get(),
                self.bookid_var.get(),
                self.booktitle_var.get(),
                self.auther_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.daysOnBook.get(),
                self.lateratefine_var.get(),
                self.dateoverdue.get(),
                self.finallprice.get()

        ))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted sucessfully")


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
