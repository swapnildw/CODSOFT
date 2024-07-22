import tkinter
from tkinter import *
import os

root = Tk()
root.title("To-Do-List")
root.geometry("300x650+100+100")  
root.resizable(False, False)

task_list = []

def openTaskFile():
    # Check if the file exists, if not create it
    if not os.path.isfile("tasklist.txt"):
        with open("tasklist.txt", "w") as taskfile:
            pass
    
    with open("tasklist.txt", "r") as taskfile:
        tasks = taskfile.readlines()

    for task in tasks:
        if task != '\n':
            task_list.append(task.strip())
            listbox.insert(END, task.strip())

# Icon
Image_icon = PhotoImage(file="Image/task.png")
root.iconphoto(False, Image_icon)

# Top bar
TopImage = PhotoImage(file="Image/topbar.png")
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file="Image/dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=20, y=25)

noteImage = PhotoImage(file="Image/task.png")
Label(root, image=noteImage, bg="#32405b").place(x=240, y=25)

heading = Label(root, text="ALL Task", font="arial 15 bold", fg="white", bg="#32405b")
heading.place(x=110, y=20)

# Main frame
frame = Frame(root, width=300, height=50, bg="white")
frame.place(x=0, y=100)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 15", bd=0, textvariable=task)
task_entry.place(x=10, y=7)
task_entry.focus()

# Button
button = Button(frame, text="Add", font="arial 15 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=lambda: addTask())
button.place(x=200, y=0)

def addTask():
    task_content = task.get()
    if task_content != "":
        listbox.insert(END, task_content)
        task_list.append(task_content)
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(task_content + "\n")
        task.set("")

# Listbox
frame1 = Frame(root, bd=3, width=300, height=400, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('arial', 12), width=35, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

# Delete button
Delete_icon = PhotoImage(file="Image/delete.png")
Button(root, image=Delete_icon, bd=0, command=lambda: deleteTask()).pack(side=BOTTOM, pady=13)

def deleteTask():
    selected_task = listbox.curselection()
    if selected_task:
        task_content = listbox.get(selected_task)
        task_list.remove(task_content)
        listbox.delete(selected_task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")

root.mainloop()
