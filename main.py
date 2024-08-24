import json
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("SMTP Settings")

        self.label = customtkinter.CTkLabel(self, text="SMTP Settings")
        self.label.pack(padx=20, pady=5)

        with open("config.json", "r") as json_file:
            config1 = json_file.read()
            config2 = json.loads(config1)
            sendermail = config2['sender_mail']
            senderpassword = config2['sender_password']
        self.label1 = customtkinter.CTkLabel(self, text="Sender Mail")
        self.label1.place(relx=0.02, rely=0.10)

        self.textbox1 = customtkinter.CTkTextbox(self)
        self.textbox1.place(relx=0.01, rely=0.20)
        self.textbox1.configure(width=393, height=20)
        self.textbox1.insert("0.0", sendermail)

        self.label2 = customtkinter.CTkLabel(self, text="Sender Password")
        self.label2.place(relx=0.02, rely=0.35)

        self.textbox2 = customtkinter.CTkTextbox(self)
        self.textbox2.place(relx=0.01, rely=0.45)
        self.textbox2.configure(width=393, height=20)
        self.textbox2.insert("0.0", senderpassword)


        self.button1 = customtkinter.CTkButton(self, text="Save Changes", command=self.save_changes)
        self.button1.place(relx=0.325, rely=0.70)

    def save_changes(self):
        with open("config.json", "r") as json_file:
            config = json_file.read()
        with open("config.json", "w") as json_file:
            new_config = json.loads(config)
            new_config['sender_mail'] = self.textbox1.get("0.0", "end")
            new_config['sender_password'] = self.textbox2.get("0.0", "end")
            new_config_json = json.dumps(new_config, indent=2)
            json_file.write(new_config_json)
            print("Config Saved Successfully")
            self.destroy()

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("854x480")
        self.title("MailBotter v1.0 | Idling..")
        self.minsize(width=854, height=480)
        self.maxsize(width=854, height=480)

        self.button1 = customtkinter.CTkButton(master=self, text="Settings", command=self.smtp_edit)
        self.button1.configure(width=75, height=30)
        self.button1.place(relx=0.99, rely=0.06, anchor="ne")

        self.button2 = customtkinter.CTkButton(master=self, text="Start", command=self.start_botting)
        self.button2.configure(width=75, height=30)
        self.button2.place(relx=0.01, rely=0.06, anchor="nw")

        self.button3 = customtkinter.CTkButton(master=self, text="End", command=self.end_botting)
        self.button3.configure(width=75, height=30)
        self.button3.place(relx=0.12, rely=0.06, anchor="nw")

        self.textbox = customtkinter.CTkTextbox(master=self)
        self.textbox.configure(width=800, height=390, state="disabled")
        self.textbox.place(relx=0.03, rely=0.15)

        self.textbox2 = customtkinter.CTkTextbox(master=self)
        self.textbox2.configure(width=550, height=30)
        self.textbox2.place(relx=0.22, rely=0.06)

        self.label1 = customtkinter.CTkLabel(self, text="Receiver Mail")
        self.label1.place(relx=0.22, rely=0)

        self.toplevel_window = None

    def smtp_edit(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def start_botting(self):
        print("Starting")
    def end_botting(self):
        print("Ending")






app = App()
app.mainloop()
