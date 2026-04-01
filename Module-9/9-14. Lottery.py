import random

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['A', 'B', 'C', 'D', 'E']

winning_numbers = random.sample(numbers, 4)
winning_letter = random.choice(letters)

winning_ticket = winning_numbers + [winning_letter]

print("Enter your lottery pick (4 numbers followed by 1 letter, separated by spaces):")
print("Example: 1 3 5 7 A")
user_input = input("> ").split()

user_guess = []
for i in range(4):
    user_guess.append(int(user_input[i]))
user_guess.append(user_input[4].upper())

print(f"\nThe winning ticket was: {winning_ticket}")
print(f"Your processed guess: {user_guess}")

if set(user_guess) == set(winning_ticket):
    print("Hurray! You're a winner!")
else:
    print("Boo Hoo, better luck next time.")
