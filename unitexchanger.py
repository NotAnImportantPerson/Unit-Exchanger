import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def miles_to_km(miles):
    return miles * 1.60934

def km_to_miles(km):
    return km / 1.60934

def pounds_to_kg(pounds):
    return pounds * 0.453592

def kg_to_pounds(kg):
    return kg / 0.453592

def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm / 2.54

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def convert():
    try:
        value = float(entry_value.get())
        conversion = conversion_type.get()

        if conversion == "Miles to Kilometers":
            result = miles_to_km(value)
        elif conversion == "Kilometers to Miles":
            result = km_to_miles(value)
        elif conversion == "Pounds to Kilograms":
            result = pounds_to_kg(value)
        elif conversion == "Kilograms to Pounds":
            result = kg_to_pounds(value)
        elif conversion == "Inches to Centimeters":
            result = inches_to_cm(value)
        elif conversion == "Centimeters to Inches":
            result = cm_to_inches(value)
        elif conversion == "Fahrenheit to Celsius":
            result = fahrenheit_to_celsius(value)
        elif conversion == "Celsius to Fahrenheit":
            result = celsius_to_fahrenheit(value)
        else:
            messagebox.showerror("Error", "Select a conversion type")
            return

        result_label.config(text=f"Result: {result:.4f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

root = tk.Tk()
root.title("Unit Converter")
root.geometry("350x250")
root.resizable(False, False)

title_label = tk.Label(root, text="Unit Converter", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

conversion_type = ttk.Combobox(
    root,
    values=[
        "Miles to Kilometers",
        "Kilometers to Miles",
        "Pounds to Kilograms",
        "Kilograms to Pounds",
        "Inches to Centimeters",
        "Centimeters to Inches",
        "Fahrenheit to Celsius",
        "Celsius to Fahrenheit",
    ],
    state="readonly",
)
conversion_type.pack(pady=5)
conversion_type.set("Miles to Kilometers")

entry_value = tk.Entry(root, font=("Arial", 12))
entry_value.pack(pady=5)
entry_value.insert(0, "Enter value")

convert_button = tk.Button(root, text="Convert", font=("Arial", 12), command=convert)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()