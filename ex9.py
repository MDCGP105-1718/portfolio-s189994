starting_salary = 150000
semi_annual_raise = 0.07
investment_return = 0.04
down_payment = 0.25

low = 0
high = 10000
saved_percent = ((low + high)/2)
current_savings = 0
steps = 0
months = 0

print ('annual_salary:' , starting_salary)

while current_savings < down_payment:
    percent_saved = saved_percent/10000
    monthly_salary = starting_salary/12
    current_savings += current_savings*investment_return/12
    current_savings += monthly_salary*percent_saved

    if current_savings < down_payment:
        low = percent_saved

    elif current_savings > down_payment:
        high = percent_saved

        print('Best savings rate:', saved_percent)
        print('Steps in search:', steps)

    else:
        print('It is not possible to pay the down payment in three years.')

    saved_percent = (low + high)/2
    steps += 1
    months += 1
