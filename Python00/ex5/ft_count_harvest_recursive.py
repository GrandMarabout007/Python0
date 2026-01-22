def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    val = days
    days = 1

    def _count_recursive(val, days):
        if val > 0:
            print(f"Day {days}")
            _count_recursive(val-1, days+1)
    _count_recursive(val, days)
    print("Harvest time!")
