
def main():
    time = input("what time is it? ").strip().lower()
    hour = convert(time)

    if 7 <= hour <= 8:
        print("breakfast time")
    elif 12 <= hour <= 13:
        print("lunch time")
    elif 18 <= hour <= 19:
        print("dinner time")
    else:
        return



def convert(time):
    if time[-4:] == "a.m.":
        first_digit = time.split(":")[0]
        second_digit = time.split(":")[1].split(" ")[0]
        first_digit = int(first_digit)
        second_digit = int(second_digit)
        if first_digit == 12:
            first_digit = 0
        second_digit = second_digit / 60
        final_digit = first_digit + second_digit
        return final_digit
    if time[-4:] == "p.m.":
        first_digit = time.split(":")[0]
        second_digit = time.split(":")[1].split(" ")[0]
        first_digit = int(first_digit)
        second_digit = int(second_digit)
        if first_digit == 12:
            second_digit = second_digit / 60
            final_digit = first_digit + second_digit
            return final_digit
        else:
            first_digit = first_digit + 12
            second_digit = second_digit / 60
            final_digit = first_digit + second_digit
            return final_digit
    else:
        first_digit = time.split(":")[0]
        second_digit = time.split(":")[1]
        first_digit = int(first_digit)
        second_digit = int(second_digit)
        second_digit = second_digit / 60
        final_digit = first_digit + second_digit
        return final_digit


if __name__ == "__main__":
    main()
