def main():
    string = input("Type something: ")
    convert(string)

def convert(string):
    result = string.replace(":(","🙁")
    result = result.replace(":)","🙂")
    print (result)




main()

