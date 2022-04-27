import random

number = random.randint(1, 100)

print("Hi, what is your name?")
name = input("Your Name: ")

print(name+", I am thinking of a number between 1 and 100.")
print("Try to guess my number.")
guess = int(input("Enter your number: "))
count = 0

for i in range(number):
    if guess > number:
        print("Your number is too high")
        guess = int(input("Enter your number: "))
        count = count + 1
    elif guess < number:
        print("Your number is too low")
        guess = int(input("Enter your number: "))
        count = count + 1
    else:
        count = count + 1
        print("Correct!", number, "was the number and it took", count, "tries.")
        break