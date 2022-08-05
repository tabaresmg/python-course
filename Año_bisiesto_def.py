def isYearLeap(year):
    var=False
    if year > 1580:
        if (year % 4)!= 0:
            var = False
        elif (year % 100)!= 0:
            var = True
        elif (year % 400)!= 0:
            var = False
        else:
            var = True
    else:
        var = False
    return var


testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]

for i in range(len(testData)):
	year = testData[i]
	print(year,"->",end="")
	result = isYearLeap(year)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")