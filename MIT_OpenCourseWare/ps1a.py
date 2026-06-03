import math

print("*" * len("Future Value of an Ordinary Annuity with compound interest"))

print("Future Value of an Ordinary Annuity with compound interest".upper())
print("Standard Formula: FV = PMT[((1 + r)^n - 1) / r]")
print("where: \nFV = Future Value\nPMT = Fixed amount of money you invest regularly at the end of each period\nr = The interest rate per period\nn = The total number of compounding periods")


print("*" * len("Future Value of an Ordinary Annuity with compound interest"))

print("This formula is used for :")
print("Payments (Investment) that are made at the end of each period. \ne.g. saving money on the last day of the month after receiving your paycheck.")
decision = str(input("start calculating ? Y | N: ".upper()))
while decision != "N":
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))

    FV = total_cost * 0.25

    current_savings = (annual_salary / 12) * portion_saved

    r = 0.04 / 12

    numerator = math.log(1 + (FV * r) / current_savings) 
    denominator = math.log(1 + r)

    number_of_months = math.ceil(numerator / denominator)
    print("Number of months:", number_of_months)

    decision = str(input("Run again? Y | N: ".upper()))
print("Good Luck!🤞🍀🫡")