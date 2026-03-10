sandwich_orders = ['reuben', 'chicken', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    
    current_sandwich = sandwich_orders.pop()
    
    print(f"I've made your {current_sandwich} sandwich.")
    
    finished_sandwiches.append(current_sandwich)

print("\n--- Finished Sandwiches ---")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")
