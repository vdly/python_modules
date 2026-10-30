def	countdown(days, day):
	print(f"Day ", day)
	if day != days:
		countdown(days, day + 1)
	else:
		return

def	ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	day = 1

	countdown(days, day)
	print("Harvest time!")

# ft_count_harvest_recursive()