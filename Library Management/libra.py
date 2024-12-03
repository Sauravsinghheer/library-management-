from tkinter import *


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1350x750+0+0")

        # Title Label
        lbltitle = Label(
            self.root,
            text="Library Management System",
            font=("Arial", 30, "bold"),
            bg="powder blue",
            fg="green",
            bd=20,
            relief=RIDGE,
            padx=2,
            pady=6,
        )
        lbltitle.pack(side=TOP, fill=X)

        # Main Frame
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        # Left Data Frame
        DataFrameLeft = Frame(frame, bd=12, relief=RIDGE, bg="powder blue")
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        # Adding Label to the Left Frame
        lblDataFrameLeft = Label(
            DataFrameLeft,
            text="Library Membership Information",
            font=("Arial", 20, "bold"),
            bg="powder blue",
            fg="green",
        )
        lblDataFrameLeft.pack(side=TOP, fill=X)


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
