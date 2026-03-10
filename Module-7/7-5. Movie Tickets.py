prompt = "\nEnter your age to see the ticket price."
prompt += "\n(Enter 'quit' when you're finished): "

while True:
    age_input = input(prompt)
    
    if age_input == 'quit':
        break
				
    age = int(age_input)
    if age < 3:
        print("  Your ticket is free.")
    elif age <= 12:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
