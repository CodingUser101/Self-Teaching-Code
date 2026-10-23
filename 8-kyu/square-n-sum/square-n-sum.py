def square_sum(numbers):
    total = 0
    for digits in numbers:
        squared = digits ** 2
        total = total + squared
    return total