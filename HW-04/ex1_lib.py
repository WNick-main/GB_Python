def calculate(salary):
    try:
        return salary - (salary * .13)
    except TypeError:
        return


def hello(name):
    print(f'Hello, {name}')


def calculate2(hours, rate, bonus):
    """
    (Production hours * rate per hour) + bonus 
    :return: full salary
    """
    try:
        return (hours * rate) + bonus
    except TypeError:
        return
