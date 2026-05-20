import datetime

print("Enter your birthdate (DD/MM/YYYY):")
date_str = input("> ")
day, month, year = map(int, date_str.split('/'))

today = datetime.date.today()
birthday_this_year = datetime.date(today.year, month, day)

if birthday_this_year > today:
    age = today.year - year - 1
else:
    age = today.year - year

candles = "i" * (age % 10)

print(f"       ___{candles}___")
print("      |:H:a:p:p:y:|")
print("    __|___________|__")
print("   |^^^^^^^^^^^^^^^^^|")
print("   |:B:i:r:t:h:d:a:y:|")
print("   |                 |")
print("   ~~~~~~~~~~~~~~~~~~~")

leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if leap:
    print("\n" + "=" * 30)
    print("Leap year! Second cake:\n")
    print(f"       ___{candles}___")
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")

print(f"\nYou are {age} years old → {age % 10} candle(s).")
if leap:
    print("(Born in a leap year → two cakes!)")