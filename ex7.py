portion_deposit = 0.2
current_savings = 0
monthly_salary= annual_salary/12
monthly_interest = current_savings *(0.04 / 12)

total_cost = float(input("Total cost of the house"))
annual_salary= float(input("How much do you earn?"))
portion_saved= float(input("How much money do you want to save?"))

months _required = ((portion_deposit * total_cost) / ((monthly_salary * portion_saved) + monthly_interest))

print("Number of months:")
