while True:
    try:
        fraction = input("Fraction: ").strip()
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y or x < 0 or y < 0:
            continue
        elif y == 0:
            raise ZeroDivisionError
        fuel = round(x * 100 / y)
        break
    except (ValueError, ZeroDivisionError):
        pass

if fuel <= 1:
    print("E")
elif  fuel >= 99:
    print("F")
else:
    print(f"{fuel}%")
