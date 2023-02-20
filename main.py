import customtkinter
import dhooks
import json

with open("config.json", "r") as f:
    config = json.load(f)

webhook = dhooks.Webhook(url=config["webhook"])

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------------------- root 
        self.root = customtkinter.CTk()
        self.root.title("Dhooks")
        self.root.geometry("1000x400")
        self.root.minsize(1000,400)
        self.root.resizable(True, False)
# ---------------------------------------------------------------- top frame
        self.TopFrame = customtkinter.CTkFrame(master=self.root)
        self.TopFrame.pack(side='top', padx=10, pady=10, fill='both')

        self.label = customtkinter.CTkLabel(master=self.TopFrame, font=("Arial", 20), text='Webhookmsg')
        self.label.pack(side='top')

        self.switch_var = customtkinter.StringVar(value="off")
        self.switch = customtkinter.CTkSwitch(master=self.TopFrame, text="always on top", variable=self.switch_var,
                                               onvalue="on", offvalue="off", command=lambda: self.alwaysontop())
        
        self.switch.pack(pady=5, padx=10, fill="both", expand=False)

# ---------------------------------------------------------------- left frame
        self.LeftFrame = customtkinter.CTkFrame(master=self.root)
        self.LeftFrame.pack(side='left', padx=10, pady=10, fill='both', expand=True)
                        # label
        self.left_title = customtkinter.CTkLabel(master=self.LeftFrame, text="embed", font=("Arial", 30))
        self.left_title.pack(side='top', padx=10, pady=10, fill='both')
                        # button
        self.embed_button = customtkinter.CTkButton(master=self.LeftFrame, text="send embed", command=self.send_embed)
        self.embed_button.pack(side='bottom', padx=5, pady=10, fill='both')
                        # description
        self.description = customtkinter.CTkEntry(master=self.LeftFrame, placeholder_text='description')
        self.description.pack(side='bottom', padx=5, pady=5, fill='both')
                        # title
        self.embed_title = customtkinter.CTkEntry(master=self.LeftFrame, placeholder_text='title')
        self.embed_title.pack(side='bottom', padx=5, pady=5, fill='both')

        self.content = customtkinter.CTkTextbox(master=self.LeftFrame)
        self.content.pack(side='bottom', padx=5, pady=5, fill='both')
# ---------------------------------------------------------------------------------------------- end of left frame 

# ---------------------------------------------------------------- right frame
        self.RightFrame = customtkinter.CTkFrame(master=self.root)
        self.RightFrame.pack(side='left', padx=10, pady=10, fill='both', expand=True)

        self.right_title = customtkinter.CTkLabel(master=self.RightFrame, text="jus text", font=("Arial", 30))
        self.right_title.pack(side='top', padx=10, pady=10, fill='both')

        self.send_text_button = customtkinter.CTkButton(master=self.RightFrame, text="send text", command=lambda: self.send_text())
        self.send_text_button.pack(side='bottom', padx=5, pady=5, fill='both')

        self.bold_text = customtkinter.CTkTextbox(master=self.RightFrame)
        self.bold_text.pack(side='bottom', padx=5, pady=5, fill='both')
# ---------------------------------------------------------------------------------------------- end of right frame

# ---------------------------------------------------------------- end
        self.root.mainloop()

# ---------------------------------------------------------------- defines and alladat

    def alwaysontop(self):
        if self.switch_var.get() == "off":
            self.root.wm_attributes("-topmost", 0) # disable topmost

        elif self.switch_var.get() == "on":
            self.root.wm_attributes("-topmost", 1) # enable topmost

        else:
            print("error")
    
    def send_embed(self):
        webhook.send(content=self.content.get('1.0', 'end'),
                embed=dhooks.Embed(
                title=self.embed_title.get(), 
                description=self.description.get(), 
                color=0x000000))

    def send_text(self):
        webhook.send(self.bold_text.get('1.0', 'end'))


    def on_exit(self):
        self.root.destroy()
        exit()


if __name__ == "__main__":
        try:
                App()
        except KeyboardInterrupt:
                exit()
