def main():
    print("welcome to the base 1 converter\nplease enter your base")
    base = input()
    print("cool, please enter your number")
    number = input()
    number = convertnumber(number, base)
    output = makebaseone(number)
    print("your base 1 number is:\n%s" % output)


def makebaseone(number):
    output = ""
    count = 1
    number = int(number)
    while number != 0:
        if count % 5 == 0:
            output = output + "0 "
        if count % 5 != 0:
            output = output + "0"
        if count % 100 == 0:
            output = output + "\n"
        count += 1
        number -= 1
    return output


def convertnumber(number, base):
    inputcheck(base)
    base = int(base)

    num = 0
    i = 0
    power = len(number) - 1

    while i < len(number):
        if number[i].isnumeric():
            num += int(number[i]) * pow(base, power)
        else:
            num += (-55 + ord(number[i].upper())) * pow(base, power)
        power -= 1
        i += 1
    return num


def inputcheck(number):
    if number.isnumeric():
        return
    else:
        raise ValueError("please put a better input")


if __name__ == "__main__":
    main()
