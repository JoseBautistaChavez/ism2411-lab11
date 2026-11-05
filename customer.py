# --- Self Reflection Questions ---
# 1. .get() prevents programs from crashing for errors. For instance, in a dictionary,
#    customers who signed up for a rewards program without a phone number (missing value)
#    wouldn't stop the program from continuing to print out the list. Choosing bracket
#    notation allows you to check for errors or missing data. In the same example, you
#    could choose to remove customers without a phone number and later mandate it so
#    the program will be able to continue printing with no exceptions.
# 2. 
#    
#    

# --- Exercise  1 ---
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

# --- Exercise  2 ---
print("--- Exercise  2 ---")
customer["phone"] = "555-5555" # Adding a new key-value pair to the dictionary
print(customer)
customer["tier"] = "platinum" # Updating the value of an existing key
del customer["Name"]
print(customer)
print(customer.get("ytp_spend", 0))

# --- Exercise  3 ---
print("--- Exercise  3 ---")
print(customer.get("email", "no email on file"))
# try:
#     print(customer["email"])
# except KeyError as error:
#     print("KeyError caught: ", error)

# --- Exercise  4 ---
print("--- Exercise  4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")
for something in customer:
    print(something)

# --- Exercise  5 ---
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

# --- Exercise  6 ---
print("--- Exercise  6 ---")
customers = [
    {"name": "Bob", "tier": "silver", "ytp_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytp_spend": 8750},
    {"name": "David", "tier": "bronze", "ytp_spend": 450}
]
for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record["name"]} ({record["tier"]}): ${discount:.2f}")

# --- Exercise  7 ---
print("--- Exercise  7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product_name, product_details in catalog.items():
    if product_details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {product_details["stock"]} left")

# --- Exercise  8 ---
print("--- Exercise  8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount
print(sales_by_region)
for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")