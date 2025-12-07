import tkinter as tk
from tkinter import messagebox
import secrets
import string

# Secure Password Generator - Grey & Black Themed GUI

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("420x360")
        self.root.resizable(False, False)
        self.root.config(bg="#2b2b2b")

        # Title
        tk.Label(root, text="Secure Password Generator", font=("Arial", 16, "bold"), bg="#2b2b2b", fg="white").pack(pady=10)

        # Frame for options
        opts = tk.Frame(root, bg="#2b2b2b")
        opts.pack(pady=5)

        self.var_upper = tk.BooleanVar(value=True)
        self.var_lower = tk.BooleanVar(value=True)
        self.var_digits = tk.BooleanVar(value=True)
        self.var_symbols = tk.BooleanVar(value=True)

        tk.Checkbutton(opts, text="Uppercase (A-Z)", variable=self.var_upper, bg="#2b2b2b", fg="white", selectcolor="#3c3c3c", activebackground="#2b2b2b").grid(row=0, column=0, sticky="w", padx=10, pady=4)
        tk.Checkbutton(opts, text="Lowercase (a-z)", variable=self.var_lower, bg="#2b2b2b", fg="white", selectcolor="#3c3c3c", activebackground="#2b2b2b").grid(row=0, column=1, sticky="w", padx=10, pady=4)
        tk.Checkbutton(opts, text="Digits (0-9)", variable=self.var_digits, bg="#2b2b2b", fg="white", selectcolor="#3c3c3c", activebackground="#2b2b2b").grid(row=1, column=0, sticky="w", padx=10, pady=4)
        tk.Checkbutton(opts, text="Symbols (!@#...)", variable=self.var_symbols, bg="#2b2b2b", fg="white", selectcolor="#3c3c3c", activebackground="#2b2b2b").grid(row=1, column=1, sticky="w", padx=10, pady=4)

        # Length
        len_frame = tk.Frame(root, bg="#2b2b2b")
        len_frame.pack(pady=8)
        tk.Label(len_frame, text="Length:", bg="#2b2b2b", fg="white").pack(side=tk.LEFT, padx=(10,5))
        self.length_var = tk.IntVar(value=16)
        self.length_spin = tk.Spinbox(len_frame, from_=4, to=64, width=5, textvariable=self.length_var, font=("Arial", 12), bg="#3c3c3c", fg="white", bd=2)
        self.length_spin.pack(side=tk.LEFT)

        # Password display
        out_frame = tk.Frame(root, bg="#2b2b2b")
        out_frame.pack(pady=10, fill=tk.X, padx=12)
        self.pass_entry = tk.Entry(out_frame, font=("Arial", 14), bg="#3c3c3c", fg="white", bd=4, justify="center")
        self.pass_entry.pack(fill=tk.X, expand=True, side=tk.LEFT, padx=(0,8))

        copy_btn = tk.Button(out_frame, text="Copy", command=self.copy_password, width=8, bg="#4b4b4b", fg="white", activebackground="#5c5c5c")
        copy_btn.pack(side=tk.LEFT)

        # Buttons
        btn_frame = tk.Frame(root, bg="#2b2b2b")
        btn_frame.pack(pady=6)

        gen_btn = tk.Button(btn_frame, text="Generate", command=self.generate_password, width=12, bg="#4b4b4b", fg="white", activebackground="#5c5c5c")
        gen_btn.grid(row=0, column=0, padx=8)

        clear_btn = tk.Button(btn_frame, text="Clear", command=self.clear_output, width=12, bg="#4b4b4b", fg="white", activebackground="#5c5c5c")
        clear_btn.grid(row=0, column=1, padx=8)

        self.status = tk.Label(root, text="Select options and click Generate", bg="#2b2b2b", fg="#bfbfbf")
        self.status.pack(pady=(8,0))

    def generate_password(self):
        length = int(self.length_var.get())
        char_pool = ""
        if self.var_upper.get():
            char_pool += string.ascii_uppercase
        if self.var_lower.get():
            char_pool += string.ascii_lowercase
        if self.var_digits.get():
            char_pool += string.digits
        if self.var_symbols.get():
            # a safe set of symbols
            char_pool += "!@#$%^&*()-_=+[]{};:,.<>?"

        if not char_pool:
            messagebox.showwarning("No characters selected", "Please select at least one character type.")
            return

        # Use secrets.choice for cryptographic randomness
        password = ''.join(secrets.choice(char_pool) for _ in range(length))
        self.pass_entry.delete(0, tk.END)
        self.pass_entry.insert(0, password)
        self.status.config(text=f"Generated {length}-char password")

    def copy_password(self):
        pwd = self.pass_entry.get()
        if not pwd:
            messagebox.showinfo("Nothing to copy", "Generate a password first.")
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(pwd)
        self.status.config(text="Password copied to clipboard")

    def clear_output(self):
        self.pass_entry.delete(0, tk.END)
        self.status.config(text="Cleared")

if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()