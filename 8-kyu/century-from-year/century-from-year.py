def century(year):
    yearAmount = year // 100
    if (year % 100 != 0 ):
        return yearAmount + 1
    else:
        return yearAmount
    