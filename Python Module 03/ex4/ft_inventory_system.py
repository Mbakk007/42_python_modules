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
print("=== Current Inventory ===")
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

    print("=== Inventory Statistics ===")
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

print("=== Item Categories ===")
print("Moderate:", moderate)
print("Scarce:", scarce)

#
#
#
#
#