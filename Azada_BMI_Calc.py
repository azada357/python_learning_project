from tkinter import *

# tk()--- Create main window
window = Tk()
window.title("BMI Calculator")  # Set window title
# Set background color and padding
window.config(bg="orange", padx=20, pady=20)
# Set minimum size for layout consistency
window.minsize(width=400, height=300)

my_label = Label(text="Calculate BMI", font=(
    "Times New Roman", 20, "bold"))  # Label for title
my_label.grid(row=0, column=0)
# calculatr BMI
# Height Input
height_label = Label(window, text="Height (m):", font=(
    "Times New Roman", 14))  # Height label
height_label.grid(row=1, column=0, sticky="e", padx=10,
                  pady=10)  # Grid placement ,Sticky east

height_entry = Entry(window, width=15, font=(
    "Times New Roman", 14), justify="center")  # Height entry field
height_entry.grid(row=1, column=1, padx=10, pady=10)  # Cursor starts here


# Weight Input
weight_label = Label(window, text="Weight (kg):", font=(
    "Times New Roman", 14))  # Weight label
weight_label.grid(row=2, column=0, sticky="e",
                  padx=10, pady=10)  # Grid placement
weight_entry = Entry(window, width=15, font=(
    "Times New Roman", 14), justify="center")  # Weight entry field
weight_entry.grid(row=2, column=1, padx=10, pady=10)  # Cursor starts here
# Result Label
result_label = Label(window, text="", font=(
    "Times New Roman", 16, "bold"), fg="red")  # Result label
result_label.grid(row=4, column=0, columnspan=2, pady=20)  # Grid placement
# BMI Category Label
category_label = Label(window, text="", font=(
    "Times New Roman", 14, "bold"), fg="green")  # Category label
category_label.grid(row=5, column=0, columnspan=2)  # Grid placement

# calculate function


def calculate_bmi():
    try:  # Get user
        height = float(height_entry.get())
        weight = float(weight_entry.get())
    except ValueError:                      # Handle non-numeric input
        result_label.config(text="Invalid input. Please enter numbers.")
        category_label.config(text="")
        return

    if height <= 0 or weight <= 0:  # Check for valid inputs
        raise ValueError("Height and weight must be positive.")

    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)

    # Determine category
    if bmi < 18.5:
        category = "Underweight"
        color = "blue"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        color = "green"
    elif 25 <= bmi < 30:
        category = "Overweight"
        color = "orange"
    else:
        category = "Obesity"
        color = "red"

# Update labels
    result_label.config(text=f"Your BMI: {bmi}", fg=color)
    category_label.config(text=f"Category: {category}", fg=color)


def clear_fields():
    height_entry.delete(0, END) 
    weight_entry.delete(0, END)
    result_label.config(text="")
    category_label.config(text="")
    height_entry.focus()

 # Buttons
button_window = Frame(window)
button_window.grid(row=3, column=0, columnspan=2, pady=20)

calc_button = Button(button_window, text="Calculate BMI", command=calculate_bmi, font=("Arial", 12, "bold"), bg="blue", fg="white", padx=20)
calc_button.grid(row=0, column=0, padx=10)

clear_button = Button(button_window, text="Clear", command=clear_fields, font=("Arial", 12), bg="brown", fg="white", padx=20)
clear_button.grid(row=0, column=1, padx=10)

window.mainloop()
