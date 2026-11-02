print("--- Exercise  1 ---")
customer = {
    "name": "Alice", # Key : Value ,
    "Name": "NotAlice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400
}
print (customer["name"])
print (customer["email"])
print (customer["tier"])
print (customer["ytd_spend"])

print("--- Exercise  2 ---")
customer["phone"] = "555-5555" # Adding a new key-value pair to the dictionary
print(customer)
customer["tier"] = "platinum" # Updating the value of an existing key
del customer["Name"]
print(customer)
print(customer.get("ytp_spend", 0))

print("--- Exercise  3 ---")
print(customer.get("email", "no email on file"))
# try:
#     print(customer["email"])
# except KeyError as error:
#     print("KeyError caught: ", error)

print("--- Exercise  4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")
for something in customer:
    print(something)

print("--- Exercise  5 ---")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.1,
    "platinum": 0.15
}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer["tier"]}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")

print("--- Exercise  6 ---")


print("--- Exercise  7 ---")


print("--- Exercise  8 ---")