import customtkinter as ctk
import requests

# Function to fetch exchange rate
def get_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    try:
        response = requests.get(url)
        data = response.json()
        rate = data["rates"].get(to_currency.upper())
        return rate
    except:
        return None

# Function to perform conversion
def convert():
    from_curr = from_currency_entry.get().upper()
    to_curr = to_currency_entry.get().upper()
    try:
        amount = float(amount_entry.get())
        rate = get_rate(from_curr, to_curr)

        if rate:
            result = amount * rate
            result_label.configure(text=f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}")
        else:
            result_label.configure(text="❌ Invalid currency code.")
    except:
        result_label.configure(text="❌ Please enter a valid number.")

# GUI Setup
ctk.set_appearance_mode("dark")  # "light", "dark", or "system"
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("💱 Currency Converter")
app.geometry("400x350")

title = ctk.CTkLabel(app, text="Currency Converter", font=("Arial", 24))
title.pack(pady=20)

from_currency_entry = ctk.CTkEntry(app, placeholder_text="From Currency (e.g. USD)")
from_currency_entry.pack(pady=10)

to_currency_entry = ctk.CTkEntry(app, placeholder_text="To Currency (e.g. INR)")
to_currency_entry.pack(pady=10)

amount_entry = ctk.CTkEntry(app, placeholder_text="Amount")
amount_entry.pack(pady=10)

convert_button = ctk.CTkButton(app, text="Convert", command=convert)
convert_button.pack(pady=15)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 18))
result_label.pack(pady=10)

app.mainloop()
