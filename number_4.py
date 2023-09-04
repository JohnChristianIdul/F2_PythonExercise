# Write the following functions
# def binaryToN(bin, type):

# def decToHex(dec):

# def main() – call all the function
def decToBinary(dec):
    if dec == 0:
        return "0"

    binary = ""
    while dec > 0:
        remainder = dec % 2
        binary = str(remainder) + binary
        dec = dec // 2

    return binary


def binaryToN(bin, type):
    decimal = 0
    base = 1

    # Convert binary to decimal
    for digit in reversed(bin):
        if digit == '1':
            decimal += base
        base *= 2

    if type == "dec":
        return decimal
    elif type == 'oct':
        octal = ""
        while decimal > 0:
            remainder = decimal % 8
            octal = str(remainder) + octal
            decimal = decimal // 8
        return octal
    elif type == 'hex':
        hexadecimal = ""
        while decimal > 0:
            remainder = decimal % 16
            if remainder < 10:
                hexadecimal = str(remainder) + hexadecimal
            else:
                hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
            decimal = decimal // 16
        return hexadecimal



def decToOctal(dec):
    if dec == 0:
        return "0"

    octal = ""
    while dec > 0:
        remainder = dec % 8
        octal = str(remainder) + octal
        dec = dec // 8

    return octal

def decToHex(dec):
    if dec == 0:
        return "0"

    hex = ""
    while dec > 0:
        remainder = dec % 16
        hex = str(remainder) + hex
        dec = dec // 16

    return hex

def main():
    decimal_number = int(input("Enter a decimal number: "))
    b = decToBinary(decimal_number)
    o = decToOctal(decimal_number)
    h = decToHex(decimal_number)
    print("The binary representation of", decimal_number, " is ", b)
    print("The octal representation of", decimal_number, " is ", o)
    print("The hexadecimal representation of", decimal_number, " is ", h)

    binary_number = int(input("Enter a binary number: "))
    t = input("Convert binary to what type (dec/oct/hex): ")
    n = binaryToN(binary_number, t)
    if t == "dec":
        print("The decimal representation of", binary_number, " is ", n)
    elif t == "oct":
        print("The octal representation of", binary_number, " is ", n)
    elif t == "hex":
        print("The hexadecimal representation of", binary_number, " is ", n)

main()
