income = int(input("Please input a income: "))
if income <= 100000:
    salary = 0.1*income
    print(salary)
elif income <= 200000:
    salary = 10000+(income-100000)*0.075
    print(salary)
elif income <= 400000:
    salary = 17500+(income-200000)*0.05
    print(salary)
elif income <= 600000:
    salary = 27500+(income-400000)*0.03
    print(salary)
elif income <= 1000000:
    salary = 33500+(income-600000)*0.015
    print(salary)
elif income > 1000000:
    salary = 39500+(income-1000000)*0.01
    print(salary)
