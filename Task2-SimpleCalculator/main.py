import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.label = tk.Label(root, text="Enter expression (num_1 operator num_2):")
        self.label.pack()

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="Result will be shown here")
        self.result_label.pack()

    def calculate(self):
        expression = self.entry.get()
        try:
            val1, oper, val2 = expression.split()
            val1 = float(val1)
            val2 = float(val2)

            if oper == '+':
                result = val1 + val2
            elif oper == '-':
                result = val1 - val2
            elif oper == '*' or oper == 'x':
                result = val1 * val2
            elif oper == '/':
                result = val1 / val2
            else:
                result = "Invalid operator choice!"
            
            self.result_label.config(text=f"Result: {val1} {oper} {val2} = {result}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid expression in the format 'num_1 operator num_2'")
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Division by zero is not possible!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
