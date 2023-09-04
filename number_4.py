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
    power = 0

    for bit in reversed(str(bin)):
        if bit == '1':
            decimal += 2 ** power
        power += 1
        print("bit: ", bit)
        print("power: ",power)
        print("decimal: ",decimal)

    if type == "dec":
        return decimal
    elif type == "oct":
        return decToOctal(decimal)
    elif type == "hex":
        return decToHex(decimal)


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
