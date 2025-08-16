def main():
    string = input("type: ")
    print (spaces(string))

def spaces(variable):
    i = 0
    result = ""
    for letter in variable:
        if letter.isupper():
            result += "_" + letter.lower()

        else:
            result += letter
    return result


main()
