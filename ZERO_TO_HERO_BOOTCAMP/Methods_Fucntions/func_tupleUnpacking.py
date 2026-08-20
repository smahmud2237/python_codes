'''

'''
stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]
for item in stock_prices:
    print(item)
for ticker,price in stock_prices:
    print(price+(0.1*price))
#---------------------------=============>O<============---------------------------#
# Given, Employee name with work hours. Print the best employee name and work hours who works more work hour on the output.
given_work_hours = [('Abu', 1000), ('Bilal', 3000), ('Mustakin', 2500)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    # Return
    return (employee_of_month, current_max)
result = employee_check(given_work_hours)
print(result)
