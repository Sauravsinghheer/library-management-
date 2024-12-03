from tkinter import ttk, messagebox
from tkinter import *
import mysql.connector
import datetime

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1350x750+0+0")

        # ========================= VARIABLES ===============================
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.auther_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysOnBook = StringVar()
        self.lateratefine_var = StringVar()
        self.dateoverdue = StringVar()
        self.finallprice = StringVar()

        # ========================= TITLE LABEL ============================
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

        # ========================= MAIN FRAME ============================
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1350, height=400)

        # ===================== DATA FRAME LEFT ===========================
        DataFrameLeft = LabelFrame(
            frame,
            text="Library Membership Information",
            bg="powder blue",
            fg="green",
            bd=12,
            relief=RIDGE,
            font=("times new roman", 12, "bold"),
        )
        DataFrameLeft.place(x=0, y=5, width=850, height=350)

        lblMember = Label(
            DataFrameLeft,
            bg="powder blue",
            text="Member Type",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(
            DataFrameLeft,
            textvariable=self.member_var,
            font=("times new roman", 12, "bold"),
            width=20,
            state="readonly",
        )
        comMember["values"] = ("Admin Staff", "Student", "Lecturer")
        comMember.current(0)
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(
            DataFrameLeft,
            bg="powder blue",
            text="PRN No:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(
            DataFrameLeft,
            font=("times new roman", 12, "bold"),
            textvariable=self.prn_var,
            width=22,
        )
        txtPRN_No.grid(row=1, column=1, padx=2, pady=6)

        # Other widgets truncated for brevity...

        # ============================== BUTTONS ==============================
        FrameButton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameButton.place(x=0, y=530, width=1350, height=70)

        btnAddData = Button(
            FrameButton,
            command=self.add_data,
            text="Add Data",
            font=("times new roman", 12, "bold"),
            width=20,
            bg="blue",
            fg="white",
        )
        btnAddData.grid(row=0, column=0, padx=10, pady=10)

        btnShowData = Button(
            FrameButton,
            command=self.fetch_data,
            text="Show Data",
            font=("times new roman", 12, "bold"),
            width=20,
            bg="blue",
            fg="white",
        )
        btnShowData.grid(row=0, column=1, padx=10, pady=10)

        btnUpdate = Button(
            FrameButton,
            command=self.update_data,
            text="Update",
            font=("times new roman", 12, "bold"),
            width=20,
            bg="blue",
            fg="white",
        )
        btnUpdate.grid(row=0, column=2, padx=10, pady=10)

        btnDelete = Button(
            FrameButton,
            command=self.delete_data,
            text="Delete",
            font=("times new roman", 12, "bold"),
            width=20,
            bg="blue",
            fg="white",
        )
        btnDelete.grid(row=0, column=3, padx=10, pady=10)

        btnReset = Button(
            FrameButton,
            command=self.reset_data,
            text="Reset",
            font=("times new roman", 12, "bold"),
            width=20,
            bg="blue",
            fg="white",
        )
        btnReset.grid(row=0, column=4, padx=10, pady=10)

        btnExit = Button(
            FrameButton,
            command=self.exit_system,
            text="Exit",
            font=("times new roman", 12, "bold"),
            width=20,
            bg="blue",
            fg="white",
        )
        btnExit.grid(row=0, column=5, padx=10, pady=10)

    # ============================== FUNCTIONS ==============================
    def add_data(self):
        # Add data to database
        pass

    def fetch_data(self):
        # Fetch data from database
        pass

    def update_data(self):
        # Update data in database
        pass

    def delete_data(self):
        # Delete data from database
        pass

    def reset_data(self):
        # Reset form fields
        pass

    def exit_system(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
