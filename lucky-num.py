from pynotifier import Notification
from random import randint

num = randint(0, 10)

print("Hey there this program will help you finding your lucky number from 1-10 for today ")
lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))


if num >= lower and num <= upper:
    print("Yes, the number is in between", lower, "and", upper)
else:
    print("No, the number is in between", lower, "and", upper)


lower = int(input("Rethink and Renter Lower bound: "))
upper = int(input("Rethink and Renter Upper bound: "))


if num >= lower and num <= upper:
    print("Yes, the number is in between", lower, "and", upper)
else:
    print("No, the number is in between", lower, "and", upper)


guess = int(input("Ok finally guess the exact number: "))

if guess == num:
    notif_title = "Congratulations"
    notif_description = "Yes the number is " + str(num)
else:
    notif_title = "Oops"
    notif_description = "The number is " + str(num)

Notification(
    title=notif_title,
    description=notif_description,
    duration=5,
    urgency="normal",
).send()