import tkinter as tk
from tkinter import messagebox

class ATMApp:
    def __init__(self, root):
        self.my_balance = 5000
        self.my_pin = 4321

        # Initialize main container
        self.root = root
        self.root.title("Majid ATM Machine")
        self.root.geometry("400x400")
        self.root.configure(bg="#e3f2fd")

        # Step 1 - Login
        self.step1 = tk.Frame(self.root, bg="#e3f2fd")
        tk.Label(self.step1, text="Please enter your PIN:", font=("Arial", 14), bg="#e3f2fd").pack(pady=10)
        self.pin_input = tk.Entry(self.step1, show="*", width=20, font=("Arial", 12))
        self.pin_input.pack(pady=10)
        self.login_button = tk.Button(self.step1, text="Login", command=self.login, bg="#007BFF", fg="white", font=("Arial", 12))
        self.login_button.pack(pady=10)
        self.step1.pack()

        # Step 2 - Operations
        self.step2 = tk.Frame(self.root, bg="#e3f2fd")
        tk.Label(self.step2, text="Select an operation:", font=("Arial", 14), bg="#e3f2fd").pack(pady=10)
        self.operation_var = tk.StringVar()
        self.operation_select = tk.OptionMenu(self.step2, self.operation_var, "Withdraw Amount", "Check Balance", command=self.on_operation_select)
        self.operation_select.pack(pady=10)
        self.amount_input = tk.Entry(self.step2, width=20, font=("Arial", 12))
        self.amount_input.pack(pady=10)
        self.confirm_button = tk.Button(self.step2, text="Confirm", command=self.confirm_action, bg="#007BFF", fg="white", font=("Arial", 12))
        self.message = tk.Label(self.step2, text="", font=("Arial", 12), bg="#e3f2fd")
        self.message.pack(pady=10)

    def login(self):
        entered_pin = self.pin_input.get()
        if entered_pin.isdigit() and int(entered_pin) == self.my_pin:
            self.step1.pack_forget()
            self.step2.pack()
            self.message.config(text="Login successful!", fg="green")
        else:
            messagebox.showerror("Error", "Invalid PIN. Please try again.")

    def on_operation_select(self, operation):
        self.message.config(text="")
        if operation == "Withdraw Amount":
            self.amount_input.pack()
            self.confirm_button.pack()
        elif operation == "Check Balance":
            self.amount_input.pack_forget()
            self.confirm_button.pack_forget()
            self.message.config(text=f"Your current balance is ${self.my_balance}.", fg="blue")

    def confirm_action(self):
        operation = self.operation_var.get()
        if operation == "Withdraw Amount":
            try:
                amount = float(self.amount_input.get())
                if amount > self.my_balance:
                    self.message.config(text="Insufficient balance.", fg="red")
                else:
                    self.my_balance -= amount
                    self.message.config(text=f"Successfully withdrew ${amount}. Remaining balance: ${self.my_balance}.", fg="green")
            except ValueError:
                self.message.config(text="Please enter a valid amount.", fg="red")
        self.amount_input.delete(0, tk.END)

# Create and run the app
root = tk.Tk()
app = ATMApp(root)
root.mainloop()
