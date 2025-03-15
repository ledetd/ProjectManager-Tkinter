from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3





# DATABASE


conn = sqlite3.connect('best_pm.db')
c = conn.cursor()

c.execute(""" CREATE TABLE if not exists well_costs (
          date integer,
          project_name text,
          well_name text,
          personnel real,
          equipment real,
          pm real,
          engineering real,
          herc real)
          """)

conn.commit()
conn.close()

#Functions

def query_database():
    conn = sqlite3.connect('best_pm.db')
    c = conn.cursor()

    c.execute("SELECT * FROM well_costs")
    records = c.fetchall()

    global count
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('oddrow',))

        count += 1

    conn.commit()
    conn.close()


def clear_entries():
    date_entry.delete(0, END)
    project_entry.delete(0, END)
    well_entry.delete(0, END)
    personnel_entry.delete(0, END)
    equipment_entry.delete(0, END)
    pm_entry.delete(0, END)
    engineering_entry.delete(0, END)
    herc_entry.delete(0, END)

def select_record(event):
    #CLEAR BOXES
    date_entry.delete(0, END)
    project_entry.delete(0, END)
    well_entry.delete(0, END)
    personnel_entry.delete(0, END)
    equipment_entry.delete(0, END)
    pm_entry.delete(0, END)
    engineering_entry.delete(0, END)
    herc_entry.delete(0, END)

    #GRAB RECORD
    selected = my_tree.focus()

    values = my_tree.item(selected, 'values')

    #OUTPOT BOXES
    date_entry.insert(0, values [0])
    project_entry.insert(0, values [1])
    well_entry.insert(0, values [2])
    personnel_entry.insert(0, values [3])
    equipment_entry.insert(0, values [4])
    pm_entry.insert(0, values [5])
    engineering_entry.insert(0, values [6])
    herc_entry.insert(0, values [7])

def update_record():
    selected = my_tree.focus()
    my_tree.item(selected, text='', values=(date_entry.get(), project_entry.get(), well_entry.get(), personnel_entry.get(), equipment_entry.get(), pm_entry.get(), engineering_entry.get(), herc_entry.get(),))
    
    date_entry.delete(0, END)
    project_entry.delete(0, END)
    well_entry.delete(0, END)
    personnel_entry.delete(0, END)
    equipment_entry.delete(0, END)
    pm_entry.delete(0, END)
    engineering_entry.delete(0, END)
    herc_entry.delete(0, END)

def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)

def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)

root = Tk()
root.title('BEST - Wells')
root.geometry("1200x500")

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview",
                background = "#D3D3D3",
                foreground = "black",
                rowheight = 25,
                fieldbackground = "D3D3D3"
                )

style.map("Treeview",
          background = [('selected', "#347083")])

# Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

tree_scroll.config(command=my_tree.yview)

# Define Columns

my_tree['columns'] = ("Date", "Project Name", "Well Name", "Personnel", "Equipment", "PM", "Engineering", "HERC")

#Format Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Date", anchor=W, width=100)
my_tree.column("Project Name", anchor=W, width=140)
my_tree.column("Well Name", anchor=W, width=140)
my_tree.column("Personnel", anchor=CENTER, width=140)
my_tree.column("Equipment", anchor=CENTER, width=140)
my_tree.column("PM", anchor=CENTER, width=140)
my_tree.column("Engineering", anchor=CENTER, width=140)
my_tree.column("HERC", anchor=CENTER, width=140)

#Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Date", text="Date", anchor=W)
my_tree.heading("Project Name", text="Project Name", anchor=W)
my_tree.heading("Well Name", text="Well Name", anchor=W)
my_tree.heading("Personnel", text="Personnel", anchor=CENTER)
my_tree.heading("Equipment", text="Equipment", anchor=CENTER)
my_tree.heading("PM", text="PM", anchor=CENTER)
my_tree.heading("Engineering", text="Engineering", anchor=CENTER)
my_tree.heading("HERC", text="HERC", anchor=CENTER)

my_tree.tag_configure("oddrow", background="white")
my_tree.tag_configure("evenrow", background="#ADD8E6")

data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

date_label = Label(data_frame, text="Date")
date_label.grid(row=0, column=0, padx=10, pady=10)
date_entry = Entry(data_frame)
date_entry.grid(row=0, column=1, padx=10, pady=10)

project_label = Label(data_frame, text="Project")
project_label.grid(row=0, column=2, padx=10, pady=10)
project_entry = Entry(data_frame)
project_entry.grid(row=0, column=3, padx=10, pady=10)

well_label = Label(data_frame, text="Well")
well_label.grid(row=0, column=4, padx=10, pady=10)
well_entry = Entry(data_frame)
well_entry.grid(row=0, column=5, padx=10, pady=10)

personnel_label = Label(data_frame, text="Personnel")
personnel_label.grid(row=1, column=0, padx=10, pady=10)
personnel_entry = Entry(data_frame)
personnel_entry.grid(row=1, column=1, padx=10, pady=10)

equipment_label = Label(data_frame, text="Equipment")
equipment_label.grid(row=1, column=2, padx=10, pady=10)
equipment_entry = Entry(data_frame)
equipment_entry.grid(row=1, column=3, padx=10, pady=10)

pm_label = Label(data_frame, text="PM")
pm_label.grid(row=1, column=4, padx=10, pady=10)
pm_entry = Entry(data_frame)
pm_entry.grid(row=1, column=5, padx=10, pady=10)

engineering_label = Label(data_frame, text="Engineering")
engineering_label.grid(row=1, column=6, padx=10, pady=10)
engineering_entry = Entry(data_frame)
engineering_entry.grid(row=1, column=7, padx=10, pady=10)

herc_label = Label(data_frame, text="HERC")
herc_label.grid(row=1, column=8, padx=10, pady=10)
herc_entry = Entry(data_frame)
herc_entry.grid(row=1, column=9, padx=10, pady=10)

# Buttons

button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

add_button = Button(button_frame, text="Add Day")
add_button.grid(row=0, column=1, padx=10, pady=15)

update_button = Button(button_frame, text="Update Day", command=update_record)
update_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove Day", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Days", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All", command=remove_all)
remove_all_button.grid(row=0, column=5, padx=10, pady=10)

# move_up_button = Button(button_frame, text="Move Up")
# move_up_button.grid(row=0, column=6, padx=10, pady=10)

# move_down_button = Button(button_frame, text="Move Down")
# move_down_button.grid(row=0, column=7, padx=10, pady=10)

clear_entry_button = Button(button_frame, text="Clear Boxes", command=clear_entries)
clear_entry_button.grid(row=0, column=8, padx=10, pady=10)

my_tree.bind("<ButtonRelease-1>", select_record)

#PULL DATA FROM DB ON START
query_database()

# RUN LOOP
root.mainloop()