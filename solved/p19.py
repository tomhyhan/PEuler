def solution():
    day = 1
    sundays = 0
    # and (year % 100 != 0 or year % 400 == 0)
    for year in range(1901, 2001):
        for month in range(1,13):
            if month in [4,6,9,11]:
                day = (day + 30) % 7
            elif month == 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    day = (day + 29) % 7
                else:
                    day = (day + 28) % 7
            else:
                day = (day + 31) % 7
            sundays += 1 if day == 6 else 0

    print(sundays)
    
solution()