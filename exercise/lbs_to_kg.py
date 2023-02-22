weight = int(input('Weight: '))
unit = input('(L)bs or (k)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted}")
else:
    converted = weight / 0.45
    print("I don't know your weight")