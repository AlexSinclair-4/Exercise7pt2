def decimalToOctal(decimal):
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return int(octal)

user_input = input("Enter a decimal number: ")
if user_input.isnumeric():
    decimal = int(user_input)
    octal = decimalToOctal(decimal)
    quotient = decimal // 8
    remainder = decimal % 8
    print(f"Octal equivalent: {octal}")
    print(f"Quotient (in decimal): {quotient}")
    print(f"Remainder (in decimal): {remainder}")
else:
    print("Invalid decimal number.")