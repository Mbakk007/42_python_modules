import sys

inventory = {}

for arg in sys.argv[1:]:
    try:
        name, qty = arg.split(":")
        inventory[name] = int(qty)
    except Exception:
        pass

total_items = sum(inventory.values())
unique_types = len(inventory)
print("=== Inventory System Analysis ===")
print("Total items in inventory:", total_items)
print("Unique item types:", unique_types)
print("\n=== Current Inventory ===")
for item, qty in inventory.items():
    percent = qty / total_items * 100
    unit_str = "unit" if qty == 1 else "units"
    print(f"{item}: {qty} {unit_str} ({percent:.1f}%)")

if inventory:
    first = True
    for item, qty in inventory.items():
        if first:
            most_abundant = item
            least_abundant = item
            first = False
        else:
            if qty > inventory[most_abundant]:
                most_abundant = item
            if qty < inventory[least_abundant]:
                least_abundant = item

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_abundant} ({inventory[most_abundant]} units)")
    print(f"Least abundant: {least_abundant} ({inventory[least_abundant]}"
          f" units)")
else:
    print("=== Inventory Statistics ===")
    print("No items to analyze.")

moderate = {}
scarce = {}
for item, qty in inventory.items():
    if qty > 4:
        moderate[item] = qty
    else:
        scarce[item] = qty

print("\n=== Item Categories ===")
print("Moderate:", moderate)
print("Scarce:", scarce)

need_restock = {}
print("\n=== Management Suggestions ===")
for item, qty in inventory.items():
    if qty <= 1:
        need_restock[item] = qty
print("Restock needed:", list(need_restock.keys()))

print("\n=== Dictionary Properties Demo ===")
print("Dictionary keys:", list(inventory.keys()))
print("Dictionary values:", list(inventory.values()))

lookup = "True" if 'sword' in inventory else "False"
print("Sample lookup - 'sword' in inventory:", lookup)
