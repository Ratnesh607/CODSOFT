import tkinter as tk
from tkinter import messagebox

# Function to perform operations
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Substraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (*)":
            result = num1 * num2
        elif operation == "Division (/)":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Plese select a valid  operation")
            return

        result_label.config(text=f"Result: {result}", fg="green")

    except ValueError:
        messagebox.showerror("Error", "Plese enter valid  numbers")


# Main Window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x450")
root.configure(bg="#c7ccd4")

# Title
title = tk.Label(root, text="Calculator", font=("Arial", 18, "bold"), fg="#000000", bg="White")
title.pack(pady=15)

# Input fields
tk.Label(root, text="Enter First Number", font=("Arial", 10, "bold"), fg="#000000", bg="#f5f5f5").pack()
entry1 = tk.Entry(root, font=("Arial", 12), width=15, bg="#e8f6f3")
entry1.pack(pady=8)

tk.Label(root, text="Enter Second Number", font=("Arial", 10, "bold"), fg="#000000", bg="#f5f5f5").pack()
entry2 = tk.Entry(root, font=("Arial", 12), width=15, bg="#e8f6f3")
entry2.pack(pady=8)

# Operation Selection
operation_var = tk.StringVar(value="Select Operation")
operations = ["Addition (+)", "Substraction (-)", "Multiplication (*)", "Division (/)"]

operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.config(font=("Arial", 12, "bold"), bg="#dcdde1", fg="black", width=20)
operation_menu.pack(pady=10)

# Calculate button
calc_btn = tk.Button(root, text="Calculate", font=("Arial", 14, "bold"),
                     bg="#3498db", fg="White", activebackground="#2980b9",
                     relief="raised", bd=3, command=calculate)
calc_btn.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), fg="Black", bg="#f5f5f5")
result_label.pack(pady=15)

# Clear button
clear_btn = tk.Button(root, text="Clear", font=("Arial", 12, "bold"),
                     bg="#ff3d54", fg="White", activebackground="#c0392b",
                     relief="raised", bd=3, command=lambda: [entry1.delete(0, tk.END),
                                                             entry2.delete(0, tk.END),
                                                             result_label.config(text="Result: ")])
clear_btn.pack(pady=5)

# Run 
root.mainloop()
