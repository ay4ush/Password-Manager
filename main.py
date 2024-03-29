from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0,END)

    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- # 
def save():
    if len(password_entry.get())==0 or len(website_entry.get())==0:
        messagebox.askokcancel("fields empty","Don't leave any fields empty")  
    else:
        website = website_entry.get()
        mail = email_entry.get()
        password = password_entry.get()
        new_data={
            website:{
                "email":mail,
                "password":password
            }
        }
        website_entry.delete(0,END) 
        password_entry.delete(0,END) 
        with open("data.json","w") as file:
            json.dump(new_data, file)
        pyperclip.copy(password)
# ---------------------------- Search Password ------------------------------- #
# def search():
#     with open("data.json","r") as file:
#         json.load(file) 
#         website = website_entry.get()
#         file[website]
        
# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title("Generate Password")
window.config(padx=50,pady=50)


#canvas
logo = Canvas(width=200,height=190)
img = PhotoImage(file="logo.png")
logo.create_image(100,95,image=img)
logo.grid(row=0,column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:",padx=0)
password_label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"ayushbhalerao8@gmail.com")
password_entry = Entry()
password_entry.grid(row=3,column=1)

#Button2s   
search_button = Button(text="Search",padx=0)
search_button.grid(row=1,column=2)
generate_password = Button(text="Generate Password",padx=0,command=gen_password)
generate_password.grid(row=3,column=2) 
add_button = Button(text="add",width=29,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop() 