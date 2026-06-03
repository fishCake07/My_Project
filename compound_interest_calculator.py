import math

print("Formula used: \nOrdinary Annuity\nFV = PMT * (((1 + r)^n - 1) / r)\n\nAnnuity Due\nFV = PMT * (((1 + r)^n - 1) /yes r) * (1 + r)")
# Ask if the user is investing at the end or at the beginning of the month
timing = str(input("Are you investing at the beginning of the month? yes | no:").strip().lower())

# Ordinary Annuity
PMT = float(input("Enter monthly investment amount: "))
rate = float(input("Enter annual investment rate (6 for 6%):"))
r = (rate / 100) / 12
period = int(input("Enter number of years: "))
n = period * 12

FV = (PMT * (((1 + r)**n) - 1) / r)

# Annuity Due
if timing == "yes":
    FV = (PMT * (((1 + r)**n) - 1) / r) * (1 + r)

print("-" * 50)
print("Future Value: $", math.ceil(FV))