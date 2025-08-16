def main():
    type = input("input: ")
    output = vowels(type)
    print (output)



def vowels(string):
    vowels_list = ["a","e","i","o","u"]
    result = ""
    for letter in string:
        if letter.lower() in vowels_list:
            continue
        else:
            result = result + letter
    return result






main()
