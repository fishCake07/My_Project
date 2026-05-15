# To-do list : 
# - Add delete previous order feature
# - User choose more than one same food （changes in order and receipt)
# - Issue of non-integer input by user

# 1.Make a dictionary of menu with prices
menu = {
    '1. siew mai': 8.50,
    '2. har gok': 10.00,
    '3. har gow': 10.50,
    '4. char siew bao': 10.00,
    '5. har cheong fun': 13.50,
    '6. char siew cheong fun': 13.00,
    '7. steamed yam': 8.00,
    '8. fried yam': 8.50
}
# Declare necessary variables
order = []
user_input = []
subtotal = 0
dimsum = []
prices = []
#3. Make a addtocart() function
def addtocart():
    i = int(user_input)
    global dimsum
    # Match the user_input to the menu
    dimsum = list(menu)[i - 1]
    # Append the dimsum selected to order
    order.append(dimsum)
    
# 4. Obtain the value (price) of the selected dimsum
def calculate():
    price = menu[dimsum]  
    prices.append(price)
    print(f'{dimsum}   RM: {price:.2f}')  
    # Add every price to subtotal
    global subtotal
    subtotal += price

print('''***Type "0" once finishing ordering.***
Start typing number to order''')
# 5.Make a loop until the customer says stop
while True:
    # Customer input food choices e.g. 1, 2, 3
    #暂时隐藏 ‘-’ 非数字错误
    user_input = int(input("Select food (e.g. 2) : "))
    #t_u_i = type(user_input)
    #number = type(1)
    if user_input == 99:
        decision = str(input("Finish ordering? (yes|no): ").lower())
        if decision == 'yes':
            break
        elif decision == 'no':
            continue
    else:
        if user_input <= len(menu):
            addtocart()
            calculate()
            print(f'\nCurrent Order: {order}')
            print(f'Current Subtotal: RM {subtotal:.2f}\n')
        else: 
            print('input is too large.')
            continue

# 6. calculate Tax (16%) and Grand Total
Tax = subtotal * 0.16
Grand_Total = subtotal + Tax

# 7.Print Neat and ordered Receipt (List of Orders with their respective prices & Total incl. tax)
print(f"\n*********RECEIPT*********\n")
# loop through every item in order and prices
for index in range(len(order)):
    print(f'{order[index]}   RM {prices[index]:.2f}')

for i in range(25): print("-", end="")
print("\n")
print(f'Subtotal: RM {subtotal:.2f}')
print(f'Tax: RM {Tax:.2f}')
print(f'Grand Total: RM {Grand_Total}\n')
    
 #subtotal, tax, grand_total


