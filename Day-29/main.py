from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    rand_char = [random.choice(letters) for letter in range(nr_letters)]
    rand_symbol = [random.choice(symbols) for symbol in range(nr_symbols)]
    rand_number = [random.choice(numbers) for number in range(nr_numbers)]

    password_list = rand_char + rand_symbol + rand_number
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
#take the inputs from website, username, and password
#after clicking add we append to the txt file
#Amazon | rocco@gmail.com | password
#also need to delete the other text from the other text boxes
def save():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    entry_data = {
        website : {
            "email": user,
            "password": password
        }
    }
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty")
    else:
        try:
            with open ("data.json","r+") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                #Saving updated data
                json.dump(entry_data,data_file,indent=4)
        else:
                #Updating old data with new data
                data.update(entry_data)
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
        finally:
                website_entry.delete(0,END)
                user_entry.delete(0, END)
                password_entry.delete(0, END)

# ----------------------------Search Method --------------------------- #
def search_file():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="File not found", message="No Data File Found")
    else:
        if website in data:
            email_data = data[website].get("email")
            password_data = data[website].get("password")
            messagebox.showinfo(title=f"{website}", message=f"Email: {email_data}\nPassword: {password_data}")
        else:
            messagebox.showinfo(title="Not found", message="No details for the website exists")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#canvas image displaying the logo window,

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website_txt = Label(text="Website",)
website_txt.grid(column=0,row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1,row=1)

user_txt = Label(text="Email/Username")
user_txt.grid(column=0,row=2)

user_entry = Entry(width=35)
user_entry.grid(column=1,row=2,columnspan=2)
user_entry.insert(0,"Piccirillo.Rocco@gmail.com")

password_txt = Label(text="Password")
password_txt.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

search_button = Button(text="Search",width=13,command=search_file)
search_button.grid(column=2,row=1)
#keeps our program running
window.mainloop()