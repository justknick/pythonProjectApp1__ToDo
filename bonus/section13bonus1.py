feet_inches = input("Enter feed and inches: ")

def convert(feet_inches_local):
    parts = feet_inches_local.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254

    # f"{feet} feet and {inches} inches is equal to {meters} meters. "
    return meters

result = convert(feet_inches)

if result < 1:
    print("Kid is too small. ")
else:
    print("Kid can ride the slide. ")
