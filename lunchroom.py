sandwich_orders = ["bacon sandwich", "pastrami sandwich", "beef sandwich", 
"cheese sandwich", "grilled cheese sandwich", "ham sandwich", "pastrami sanwich", 
"pork sandwich", "tuna sandwich", "pastrami sandwich"]

finished_sandwiches = []

print("We are currently out of pastrami!\n")

while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("pastrami sandwich")

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