# century(year) plugs in a random year, I have to sort and plug in the year. 
# evern century takes the first two digits of the year and adds +1 to tens place
​
def century(year):
    actualYear = year // 100
    if year % 100 == 0:
     return actualYear
    else:
     return actualYear + 1
    
​