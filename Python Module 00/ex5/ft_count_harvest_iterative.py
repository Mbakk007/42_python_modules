def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    i = 1
    if days <= 0:
        print("Harvest time!")
        return
    while i <= days:
        print(f"Day {i}")
        i += 1
    print("Harvest time!")
