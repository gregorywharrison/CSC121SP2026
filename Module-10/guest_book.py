from pathlib import Path

path = Path('10-4. Guest Book/guest_book.txt')

guest_entries = ""

while True:
    name = input("Please enter your name (type 'quit' to exit): ")
    
    if name.lower() == 'quit':
        break
    
    print(f"Hello {name}, You have been added to the guest book!")
    
    guest_entries += f"{name}\n"

path.write_text(guest_entries)
