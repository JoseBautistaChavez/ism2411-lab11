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
try:
    print(customer["email"])
except KeyError as error:
    print("KeyError caught: ", error)

print("--- Exercise  4 ---")


print("--- Exercise  5 ---")


print("--- Exercise  6 ---")


print("--- Exercise  7 ---")


print("--- Exercise  8 ---")