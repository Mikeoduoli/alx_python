import random
number = random.randint(-10, 98)
if number > 0:
    print(f"{number}is positive")
elif number == 0:
    print(f"is zero")
else:
    print(f"is negative")
