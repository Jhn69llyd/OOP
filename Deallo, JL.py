#John Lloyd Deallo
import tkinter as tk

def add_item():
    """Add an item from the entry box to the listbox."""
    item = entry.get()
    if item:  
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END) 

def remove_item():
    """Remove the selected item from the listbox."""
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index[0])

def clear_list():
    """Clear all items from the listbox."""
    listbox.delete(0, tk.END) 

root = tk.Tk()
root.title("Listbox Example")

entry = tk.Entry(root)
entry.pack(pady=20) 

add_button = tk.Button(root, text="Add", command=add_item)
add_button.pack(pady=10)

remove_button = tk.Button(root, text="Remove", command=remove_item)
remove_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_list)
clear_button.pack(pady=10)

listbox = tk.Listbox(root)
listbox.pack(padx=20, pady=20) 
root.mainloop()
