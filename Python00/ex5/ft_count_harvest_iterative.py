def ft_count_harvest_iterative():
	days = input("Days until harvest: ")
	val = int(days)
	days = 1
	while val > 0:
		print(f"Day {days}")
		days = int(days) + 1
		val = val - 1
	print("Harvest time!")