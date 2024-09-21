# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally, a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.

answer = str(input("Would you like a Hot Dog or a Chili Dog?"))
two = "chili dog" or "Chili Dog"
if answer == "hot dog" or "Hot Dog":
        subtotal = 3.50
        topping = str(input("Toppings? yes or no?"))

        if topping == 'yes' or 'Yes':
            cheese = str(input("Cheese? Yes or No?"))
        elif cheese == "yes" or "Yes":
                subtotal = subtotal + 0.50
        if cheese == 'no' or "No":
                subtotal = subtotal + 0.0
        peppers = str(input("Peppers? Yes or No?"))
        elif peppers == "yes" or "Yes":
                subtotal = subtotal + 0.76
        if peppers == 'no' or "No":
                subtotal = subtotal + 0.0
            grilled = str(input("Grilled Onions? Yes or No?"))
        elif grilled == "yes" or "Yes":
                subtotal = subtotal + 1.00
        if grilled == 'no' or "No":
                subtotal = subtotal + 0.0
        if topping == 'No' or 'no':
            tax = subtotal * 0.07
            total = subtotal + tax
            print('Here is your receipt')
            print(subtotal)
            print(tax)
            print(total)

if answer != "chili dog" and not "Chili Dog":
    pass
else:
    print("error chose one")