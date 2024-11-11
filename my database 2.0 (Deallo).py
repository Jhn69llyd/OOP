from tkinter import *
import sqlite3

# Create the main window
root = Tk()
root.title('MyCRUD Project')
root.geometry("500x500")

# Connect to the SQLite database
def connect_db():
    return sqlite3.connect('my_database_jld.db')

# Create table if it doesn't exist
def create_table():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS myinfo (
        f_name TEXT,
        l_name TEXT,
        age INTEGER,
        address TEXT,
        email TEXT
    );
    """)
    conn.commit()
    conn.close()

create_table()

# Function to submit data to the database
def submit():
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO myinfo (f_name, l_name, age, address, email) VALUES (?, ?, ?, ?, ?)",
              (f_name.get(), l_name.get(), age.get(), address.get(), email.get()))
    conn.commit()
    conn.close()
    
    # Clear the entry fields after submission
    f_name.delete(0, END)
    l_name.delete(0, END)
    age.delete(0, END)
    address.delete(0, END)
    email.delete(0, END)

# Function to query and display records
def query():
    conn = connect_db()
    c = conn.cursor()
    
    c.execute("SELECT *, oid FROM myinfo")
    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + "\n"

    query_label.config(text=print_records)  # Update label with records
    
    conn.close()

# Function to delete a record by ID
def delete():
    conn = connect_db()
    c = conn.cursor()
    
    c.execute("DELETE FROM myinfo WHERE oid=?", (delete_box.get(),))
    
    delete_box.delete(0, END)  # Clear the delete box after deletion
    conn.commit()
    conn.close()

# Entry fields and labels
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
age = Entry(root, width=30)
age.grid(row=2, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=3, column=1, padx=20)
email = Entry(root, width=30)
email.grid(row=4, column=1, padx=20)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name")  
l_name_label.grid(row=1, column=0)
age_label = Label(root, text="Age")
age_label.grid(row=2, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=3, column=0)
email_label = Label(root, text="Email")
email_label.grid(row=4, column=0)

# Buttons
submit_btn = Button(root,text="Add Record to Database", command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=(10, 5), padx=(10, 10), ipadx=100)

query_btn = Button(root,text="Show Records", command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=(5, 10), padx=(10, 10), ipadx=137)

delete_btn = Button(root,text="Delete Record",command=delete)
delete_btn.grid(row=12,column=0,columnspan=2,pady=(10), padx=(10), ipadx=136)

delete_box = Entry(root,width=30)
delete_box.grid(row=10,column=1,padx=(20))
delete_box_label = Label(root,text="Select ID No.")
delete_box_label.grid(row=10,column=0)

query_label = Label(root,text="", justify='left')
query_label.grid(row=8,column=0,columnspan=2)

root.mainloop()
