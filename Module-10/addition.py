print("Provide two numbers, and I'll add them together.")

first_number = input("\nFirst number: ")
second_number = input("Second number: ")

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Sorry, please provide numbers to perform math. Try again.")
else:
    print(f"The sum is: {answer}")
