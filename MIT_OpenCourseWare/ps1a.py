annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost
current_savings = 0
months = 0
r = 0.04

while current_savings < down_payment:
    # Calculate this month's investment return
    monthly_return = current_savings * (r/12)

    # Calculate this month's salary savings
    monthly_savings = portion_saved * (annual_salary / 12)

    # Update total savings at the end of the month
    current_savings += monthly_return + monthly_savings
    
    # Increment the month counter
    months += 1

print("Number of months:", months)
