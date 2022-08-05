def isYearLeap(year):
    yr=False
    if year > 1580:
        if (year % 4)!= 0:
            yr = False
        elif (year % 100)!= 0:
            yr = True
        elif (year % 400)!= 0:
            yr = False
        else:
            yr = True
    else:
        yr = False
    return yr  

def daysInMonth(year, mo):
    mes=list([0,31,28,31,30,31,30,31,31,30,31,30,31])
    if isYearLeap(year)==True:
        mes[2]=29
    return mes[mo]

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]

for i in range(len(testYears)):
	year = testYears[i]
	mo = testMonths[i]
	print(year, mo, "->", end="")
	yr = daysInMonth(year, mo)
	if yr == testResults[i]:
		print("OK")
	else:
		print("Error")