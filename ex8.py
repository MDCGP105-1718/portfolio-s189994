portion_deposit = 0.20
current_savings = 0
r = 0.04
monthly_interest = current_savings*(r/12)
monthly_salary= annual_salary/12

total_cost = float(input("Total cost of the house"))
annual_salary= float(input("Enter the starting annual salary:"))
portion_saved= float(input("How much money do you want to save?"))
semi_annual_raise=float(input("By what proportion does you salary increase every six months?"))

portion_deposit = total_cost*portion_deposit
months = 0

while current_savings < total_cost*portion_deposit:
    current_savings += current_savings*(r/12)
    current_savings += monthly_salary * portion_saved
    months += 1
  monthly_salary += monthly_salary * (semi_annual_raise/12)

print("Number of months:", months)
