import tkinter as tk
from tkinter import messagebox

class InformationFormGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Information Form")
        self.root.geometry("400x300")
        self.root.configure(bg="light blue")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text="Hello! What is your name?", font=('Times New Roman', 14), bg="light blue")
        self.label.pack(pady=20)

        self.user_name = tk.Entry(self.root, font=('Times New Roman', 12), bg="white", width=30)
        self.user_name.pack()

        self.next_button = tk.Button(self.root, text="Next", command=self.get_age, font=('Times New Roman', 12))
        self.next_button.pack(side="bottom", pady=5)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_input, font=('Times New Roman', 12))
        self.clear_button.pack(side="bottom", pady=5)

        self.age = ""
        self.address = ""

    def get_age(self):
        self.user_name_input = self.user_name.get()
        if self.user_name_input == "":
            messagebox.showwarning("Warning", "Please enter your name!")
        else:
            self.label.config(text=f"Nice meeting you, {self.user_name_input}! How old are you?")
            self.user_name.config(state='disabled')
            self.next_button.config(command=self.get_address)

            self.age_entry = tk.Entry(self.root, font=('Times New Roman', 12), bg="white", width=30)
            self.age_entry.pack()

            self.next_button.pack(side="bottom", pady=5)
            self.clear_button.pack(side="bottom", pady=5)

    def get_address(self):
        self.age = self.age_entry.get()
        if self.age == "":
            messagebox.showwarning("Warning", "Please enter your age!")
        else:
            self.label.config(text="Where are you from?")
            self.age_entry.config(state='disabled')
            self.next_button.config(text="Submit", command=self.show_summary)
            self.next_button.pack(side="bottom", pady=5)

            self.address_entry = tk.Entry(self.root, font=('Times New Roman', 12), bg="white", width=30)
            self.address_entry.pack()

            self.next_button.pack(side="bottom", pady=5)
            self.clear_button.pack(side="bottom", pady=5)

    def show_summary(self):
        self.address = self.address_entry.get()
        if self.address == "":
            messagebox.showwarning("Warning", "Please enter your address!")
        else:
            summary = f"Name: {self.user_name_input}\nAge: {self.age}\nAddress: {self.address}"
            messagebox.showinfo("Summary", summary)
            self.root.destroy()

    def clear_input(self):
        self.label.config(text="Hello! What is your name?")
        self.user_name.config(state='normal')
        self.user_name.delete(0, tk.END)
        if hasattr(self, 'age_entry'):
            self.age_entry.destroy()
        if hasattr(self, 'address_entry'):
            self.address_entry.destroy()
        self.next_button.config(text="Next", command=self.get_age)

def main():
    root = tk.Tk()
    info_form = InformationFormGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
