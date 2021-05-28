sandwich_orders = ["bacon sandwich", "beef sandwich", "cheese sandwich",
"grilled cheese sandwich", "ham sandwich", "pork sandwich", "tuna sandwich"]

finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print("I made your " + current_order.title() + ".")
    finished_sandwiches.append(current_order)

print("\nThe following sandwich orders have been finished: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

print("\n")
# all orders are now in the finished_sandwiches list:
print(finished_sandwiches)