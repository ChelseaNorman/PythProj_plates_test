def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if  len(plate) <2 or len(plate)> 6:
         return False


    if plate[0].isalpha() == False or plate[1].isalpha() == False:
        return False

    i = 0
    while i < len(plate):
        if plate[i].isalpha() == False:
            if plate[i] == "0":
                return False
            else:
                break
        i += 1

    for num in plate:
        if num.isdigit():
            index = plate.index(num)
            if not plate[index:].isdigit():
                return False

    for char in plate:
        if char in ['.', ' ', '!', '?']:
            return False

    return True

if __name__ == "__main__":
    main()
