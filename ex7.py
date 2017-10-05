total_cost = float(input("Total cost of the house"))
portion_deposit = 0.20
current_savings = 0
r= 0.04
current_savings = current_savings*r/12

annual_salary= float(input("How much do you earn?"))
portion_saved= float(input("How much money do you want to save?"))
monthly_salary= annual_salary/12
p=0

while current_savings < total_cost*portion_deposit:
    current_savings =current_savings + monthly_salary *portion_saved
    current_savings =current_savings + current_savings*r/12
    p=p+1
print(f"Number of mounths:{p}")
