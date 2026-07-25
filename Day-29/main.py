from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
def generate_password():
# #---------------------------- PASSWORD GENERATOR ------------------------------- #
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(5, 7))]
    password_numbers= [choice(numbers) for _ in range(randint(2, 5))]
    password_symbols = [choice(symbols) for _ in range(randint(1, 4))]


    
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    

# #---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
            messagebox.showwarning(title="Oops",message= "Please don't leave any fields empty!")

    else:
        try:
            with open("Day-29/data.json", mode="r") as password_data_file:

                #Reading ol data
                
                data_read = json.load(password_data_file)

        except FileNotFoundError:
                with open("Day-29/data.json", mode="w") as password_data_file:
                            json.dump(new_data, password_data_file, indent=4)
            #Updating old with new data
        else:
            data_read.update(new_data)
            #saving updated data
            with open("Day-29/data.json", mode="w") as password_data_file:
                json.dump(data_read, password_data_file, indent=4)
        finally:
              website_entry.delete(0, END)
              password_entry.delete(0, END)

# ---------------------------- Find password ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("Day-29/data.json", mode="r") as password_data_file:
            data_read = json.load(password_data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message= "No Data File Found.")

            
    else:
        if website in data_read:
            email = data_read[website]["email"]
            password = data_read[website]["password"]
            messagebox.showinfo(title=website, message=f"email: {email}\npassword: {password}")
        else:
             messagebox.showinfo(title="Error", message=f"No details for {website} exists.")




#----------------------------- User Interface ---------------------------------W
#Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Canvas
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="Day-29/logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

#label
Website_label = Label(text="Website:")
Website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry =Entry(width=32)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sumit2232@gmail.com")


password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)


#button
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)


generate_pass_button = Button(text="Generate Password", width= 14, command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()

 


  












