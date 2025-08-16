def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    zero = 0
    i = 0
    num = 0
    if len(s) >= 2 and len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            for digit in s:
                if digit.isdigit():
                    num = 1

                elif not digit.isdigit() and num == 1:
                    return False

            for digit in s:
                if digit.isdigit():
                    if digit == "0" and zero == 0:
                        return False
                    zero = 1
        else:
            return False
    else:
        return False
    return True



main()
