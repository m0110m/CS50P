def main():
    while True:
        try:
            fraction = input("Fraction: ")
            fuel = convert(fraction)
            print(gauge(fuel))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y:
        raise ValueError
    elif x < 0 or y < 0:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    return round(x * 100 / y)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif  percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()


