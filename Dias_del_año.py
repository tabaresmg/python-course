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


def dayOfYear(year, mo, day):
    dias= 0
    if isYearLeap(year)==True:
       mes=[0,31,29,31,30,31,30,31,31,30,31,30,31]
       
       for i in range(len(mes[0:(mo)])):
            dias= dias+mes[i]
    else:
        mes=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(len(mes[0:(mo)])):
            dias= dias+mes[i]
    dias= dias + day
    return 'La cantidad de días corridos del año es: ', dias
       




print(dayOfYear(2000, 12, 31))