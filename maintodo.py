import tkinter as tk
from tkinter import *

root = Tk()
root.title("ToDoList")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []
image_icon = PhotoImage(file="images/task.png")
root.iconphoto(False, image_icon)
topimage = PhotoImage(file="images/topbar.png")
Label(root, image=topimage).pack()
dockimage = PhotoImage(file="images/dock.png")
Label(root, image=dockimage, bg="#32405b").place(x=30, y=25)
noteimage = PhotoImage(file="images/task.png")
Label(root, image=noteimage, bg="#32505b").place(x=20, y=25)
heading = Label(root, text="ALL TASK", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)
task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

def add_task():
    task = task_entry.get()
    if task!= "":
        listbox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except:
        pass

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=add_task)
button.place(x=300, y=0)

delete_button = Button(frame, text="DELETE", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=delete_task)
delete_button.place(x=200, y=0)

frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))
listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

root.mainloop()