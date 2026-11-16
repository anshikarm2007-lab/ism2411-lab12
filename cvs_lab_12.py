#Reflection:
# Reflection 1:
# Python and Excel can both organize data, calculate totals, and filter information.
# However, Python is better for automating repetitive tasks, processing large amounts
# of data, and running the same steps multiple times without doing everything manually.
# Excel is easier for quickly viewing data, making charts, and performing simple
# calculations without needing to write code.

# Reflection 2:
# A business could use an append-mode log file to keep track of daily sales transactions.
# Each time a sale is recorded, the program adds a new entry with the date, time, and
# sales amount. Append mode is useful because it keeps previous records instead of
# replacing them, allowing the business to maintain a history of its sales



import csv
from datetime import datetime

SALES_FILE = "sales.csv"
CLEANED_FILE = "cleaned.csv"
LOG_FILE = "run_log.txt"

print("---Exercise 1---")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}.")

print("---Exercise 2---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("---Exercise 3---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)

print("---Exercise 4---")
tota;_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader) #skip header
    for row in reader:
        product, price_str, quantity_str = row
        price = float(price_str)
        quantity = int(quantity_str)
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}") 


print("---Exercise 5---")

high_value = []
rows_read = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader) #skip header
    for row in reader:
        rows_read += 1
        product, price_str, quantity_str = row
        price = float(price_str)
        quantity = int(quantity_str)
        total = price * quantity
        if total > 100:
            high_value.append([product, f"${price:.2f}", quantity, f"${total:.2f}"])
with open(CLEANED_FILE, "W", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "price", "Quantity", "Total"])
    for row in high_value:
        writer.writerow(row)

    print(f"Wrote {len(high_value)} of {rows_read} rows to {CLEANED_FILE}.")

    print("---Exercise 6---")

    dict_total = 0
    with open(SALES_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            price = float(row["price"])
            quantity = int(row["quantity"])
            total = price * quantity
            dict_total += total
            print(f"{row['product']}: {quantity} x ${price:.2f} = ${total:.2f}")

    print(f"Total sales: ${dict_total:.2f}")


    print("---Exercise 7---")
    summary = {}

    with open(SALES_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row["product"]
            total = float(row["price"]) * int(row["quantity"])
            summary[product] = summary.get(product, 0) + total
for product in sorted (summary.keys()):
    print(f"{product}: ${summary[product]:.2f}")             

print("---Exercise 8---")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} total revenue: ${total_revenue:.2f}\n")

entries = 0
with open(LOG_FILE, "r") as f:
    for line in f:
        entries += 1
        print(line.strip())
print (f"Log entries so far: {entries}")            