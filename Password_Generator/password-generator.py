import tkinter as tk
from tkinter import messagebox , simpledialog, ttk    
import random as rd
import pyperclip 
import string

def generate_password():
    try:
        length=slider.get()
        if length<=0:
            messagebox.showerror("Error", "Length must be a positive integer.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return
    chars=""
    if uppercase.get():
        chars+=string.ascii_uppercase
    if lowercase.get():
        chars+=string.ascii_lowercase
    if digit.get():
        chars+=string.digits
    if symbols.get():
        chars+=string.punctuation
    
    if not chars:
        messagebox.showerror("Error", "Select at least one character type.")
        return
    
    password=""
    for i in range(length):
        password+= rd.choice(chars)
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0,  password)
def copy_to_clipboard():
    password=password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showinfo("Error", "No password to copy")


window=tk.Tk()
window.title("🔐🔑 Password Generator")
window.geometry("480x600")


# #creating frame 1, title message
frame1=tk.Frame(window)
frame1.pack()

label1=tk.Label(frame1, text="🔗Strong Password Generator", font=("Aerial",20))
label1.pack()

window.columnconfigure(0, weight=1)     #configures the 0th column and weight=1 means column is allowed to grow and take extra space when the window resizes

#creating frame 2, label message
frame2=tk.Frame(window)
frame2.pack()

label2=tk.Label(frame2, text="Password Length: ",font=("Aerial",12))
label2.pack()

def update_label(value):        #calling the function when everytime length changes
    value_label.config(text=value)

value_label=tk.Label(window, text="8",font=("Aerial",12),width=5,relief="solid",bd=1)       #relief->border style and bd->border width
value_label.pack()      #prints the password length in the label

slider=tk.Scale(window,     #creating a slider for input length
               from_=4,
               to=50,
               orient="horizontal",
               command=update_label,        #function call to update_label to print the output length
               length=300,
               sliderlength=20,
               highlightthickness=0
               )
slider.set(8)
slider.pack()

#creating a character types for the checkboxes(also we can use Intvar)
uppercase=tk.BooleanVar()
lowercase=tk.BooleanVar()
digit=tk.BooleanVar()
symbols=tk.BooleanVar()

#displaying the password criteria checkboxes
checkbox1=tk.Checkbutton(window, text="Include Uppercase",variable=uppercase,width=20,font=("aerial",12)).pack(pady=(30,0))
checkbox1=tk.Checkbutton(window, text="Include lowercase",variable=lowercase,width=20,font=("aerial",12)).pack()
checkbox1=tk.Checkbutton(window, text="Include digits",variable=digit,width=20,font=("aerial",12)).pack()
checkbox1=tk.Checkbutton(window, text="Include symbols",variable=symbols,width=20,font=("aerial",12)).pack()


#generate button widget for generate button
button1=tk.Button(window, text="Generate",font=("Aerial Bold",14),width=10,bg="dark grey",command=generate_password)
button1.pack(pady=20)

#creating a entry widget for printing the generated password.
password_entry=tk.Entry(window,width=30,font=("aerial",16),bg="white")
password_entry.pack()

#generate button widget for copy to clipboard button
button2=tk.Button(window,text="Copy to clipboard",font=("Aerial",14),width=20,bg="pink",command=copy_to_clipboard)
button2.pack(pady=(20,0))


def password_manager():
    

    button4=tk.Button(window, text="Saved Passwords",font=("Aerial Bold",14),command=saved_password)
    button4.pack(side="left",padx=30)

    button5=tk.Button(window,text="+Add Password",font=("Aerial Bold",14),width=20,command=add_password)
    button5.pack(side="left",padx=30)

#creating a list to store the list of password details to from the entry
saved_passwords=[]   

def saved_password():
    new_window=tk.Toplevel()
    new_window.title("Saved Passwords")
    new_window.geometry("630x300")

    frame4=tk.Frame(new_window)
    frame4.pack(pady=20)

    #defining treeview
    tree=ttk.Treeview(frame4,column=("Website","Username","Password"),show="headings")      
    tree.heading("Website",text="Website")
    tree.heading("Username",text="Username")
    tree.heading("Password",text="Password")
    tree.pack(padx=10,pady=10)

    #to save the entered password in the saved password window
    for entry in saved_passwords:
        tree.insert("","end",values=(entry["Website"],entry["Username"],entry["Password"]))

def add_password():
    new_window1=tk.Toplevel()
    new_window1.title("Add Password")
    new_window1.geometry("480x400")

    #creating new frames for label and url entry
    frame4=tk.Frame(new_window1)
    frame4.pack(pady=30)

    #url label and entry widget
    url_label = tk.Label(frame4, text="Website URL: ", font=("Aerial Bold", 16))
    url_label.pack(pady=(10, 5))  #padding above 10 and below 5

    url_entry = tk.Entry(frame4, width=30, font=("Aerial", 16))
    url_entry.pack(pady=(0, 10))  #padding above 0 and below 10

    # Username label and entry widget
    username_label = tk.Label(frame4, text="Username: ", font=("Aerial Bold", 16))
    username_label.pack(pady=(10, 5))  #padding above 10 and below 5

    username_entry = tk.Entry(frame4, width=30, font=("Aerial", 16))
    username_entry.pack(pady=(0, 10))  #padding above 0 and below 10

    # password label and entry wiget
    password_label=tk.Label(frame4, text="Password: ",font=("Aerial Bold",16))
    password_label.pack(pady=(10,5))

    password_entry=tk.Entry(frame4,width=30, font=("Aerail",16))
    password_entry.pack(pady=(0,10))

    def save_password():
        website=url_entry.get()
        username=username_entry.get()
        password=password_entry.get()

        if website and username and password:
            saved_passwords.append({"Website":website,"Username":username,"Password":password})
            messagebox.showinfo("Saved","Password saved successfully")
            new_window1.destroy()   #closes the opened window after saving
            return saved_password
        else:
            messagebox.showerror("Error","Error")






    save_button=tk.Button(frame4, text=" SAVE ",font=("areial bold",20),fg="red",bg="#333333",width=15,command=save_password)
    save_button.pack(pady=(10,0))
    
frame3=tk.Frame(window)
frame3.pack()

button3=tk.Button(frame3, text="Password Management",font=("Bold",16),width=30,fg="red",command=password_manager)       #creating a password manager to store and add passswords.
button3.pack(pady=(30,0))




window.mainloop()