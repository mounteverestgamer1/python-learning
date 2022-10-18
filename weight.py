weight  = int(input ('weight: '))
unit = input ('(l)bs or (k)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print (f" you are {converted} kilos")
else:
    converted =weight / 0.45
    print(f"you are{converted} pounds")