temp =  input('Which temperature whould you like to convert, for example: 50F, 20C: ')
degree = int(temp[: -1])
conv = temp[-1]

if conv.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    d_conv = 'Farenheit'
elif conv.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    d_conv = "Celsius"
else:
    print("unable to convert")
    quit()
print ("The current temperature in" , d_conv, "is" , result)

