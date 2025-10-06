months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            month, day, y = date.split("/")
            m = int(month)
            d = int(day)
            if m > 12 or d > 31:
                continue
            print(f"{y}-{m:02}-{d:02}")
            break
        elif "," in date:
            month, day, y = date.split(" ")
            d = int(day.replace(",", ""))
            if month in months:
                m = months.index(month) + 1
            else:
                continue
            if d > 31:
                continue
            print(f"{y}-{m:02}-{d:02}")
            break
        else:
            continue

    except ValueError:
        pass
