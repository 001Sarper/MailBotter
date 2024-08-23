from doctest import master
from turtledemo.penrose import start

import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("854x480")
app.title("MailBotter v1.0 | github.com/001Sarper | Idling..")
app.minsize(width=854, height=480)
app.maxsize(width=854, height=480)


def smtp_edit():
    print("button pressed")

def start_botting():
    print("Starting")

def end_botting():
    print("Ending")



button1 = customtkinter.CTkButton(master=app, text="Edit SMTP Values", command=smtp_edit())
button1.configure(width=75, height=40)
button1.place(relx=0.99, rely=0.01, anchor="ne")

button2 = customtkinter.CTkButton(master=app, text="Start Botting", command=start_botting())
button2.configure(width=75, height=40)
button2.place(relx=0.01, rely=0.01, anchor="nw")

button3 = customtkinter.CTkButton(master=app, text="Stop Botting", command=end_botting())
button3.configure(width=75, height=40)
button3.place(relx=0.12, rely=0.01, anchor="nw")

textbox = customtkinter.CTkTextbox(master=app)
textbox.configure(width=800, height=400, state="disabled")
textbox.place(relx=0.03, rely=0.13)


app.mainloop()
