def main():
    time = input("What time is it? ").strip()
    t = convert(time)
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    else:
        print("dinner time")

def convert(time):
    hour, minutes = time.split(":")
    h = float(hour)
    m = float(minutes) / 60
    return h+m


if __name__ == "__main__":
    main()
