# INPUT and PRINT
name = input("Enter your name: ")
print(f"Welcome {name}!")

# Print a message with the company's core values: Integrity, Innovation, and Teamwork.
print(
    "Our company's core values are:\n- Reliability\n- Respect\n- Striving for excellence"
)
print("Our company's core values are:")
print("- Reliability")
print("- Respect")
print("- Striving for excellence")

print("Our company's core values are:", end="")
print("Reliability, ", end="")
print("Respect, ", end="")
print("Strive for excellence.")

# Calculate the exchange rate from RON to EUR
amount_ron = input("Amount in RON: ")
exchange_rate = 4.98
amount_eur = (
    float(amount_ron) / exchange_rate
)  # let the error be raised to find a solution
print(amount_eur)  # too many decimals
print(round(amount_eur, 2))
