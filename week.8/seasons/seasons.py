from datetime import date
import sys
import re
import inflect
p = inflect.engine()

def main():
    d = input("Date of Birth: ").strip()
    D = return_date(d)
    time_difference = date.today() - D
    minutes_difference = time_difference.days * 24 * 60
    print(f"{p.number_to_words(minutes_difference, andword="").capitalize()} minutes")


def return_date(d):
    if matches := re.search(r'^(\d\d\d\d)-(\d\d)-(\d\d)$', d):
        year = int(matches.group(1))
        month = int(matches.group(2))
        day = int(matches.group(3))
        return date(year, month, day)
    else:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
