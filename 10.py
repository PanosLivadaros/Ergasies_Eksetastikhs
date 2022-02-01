def integer_multiple(z):
    global count2, count3, count5, count7
    if z % 2 == 0:
        count2 += 1
    if z % 3 == 0:
        count3 += 1
    if z % 5 == 0:
        count5 += 1
    if z % 7 == 0:
        count7 += 1

count2 = count3 = count5 = count7 = 0
decimal_array = []
file = input("Give a .txt file to process: \n")
with open(file, "r") as f:
    binary_array = []
    for line in f:
        for character in line:
            temp = bin(int.from_bytes(character.encode(), "big"))
            temp = temp.strip("0b")
            if len(temp) < 7:
                temp = "0" * (7-len(temp)) + temp
            binary_array.append(temp[:2] + temp[5:])
if len(binary_array) % 4 != 0 and len(binary_array) < 4:
    decimal_array = int("".join(binary_array), 2)
else:
    num = len(binary_array) / 4
    if num % 1 != 0:
        num = int(num - num % 1) + 1
    else:
        num = int(num - num % 1)
    for i in range(num):
        if i == num:
            decimal_array.append(int("".join(binary_array[:5]), 2))
        elif i == num:
            decimal_array.append(int("".join(binary_array[(4 * i + 1):]), 2))
        else:
            decimal_array.append(int("".join(binary_array[(4 * i + 1):(4 * (i + 1) + 1)]), 2))
if type(decimal_array) == int:
    integer_multiple(decimal_array)
    print("Το ποσοστό των ζυγών είναι:", count2 * 100, "% , το ποσοστό των ακέραιων πολλαπλάσιων του 3 είναι:", count3 * 100, "%, το ποσοστό των ακέραιων πολλαπλασίων του 5 είναι:", count5 * 100, "% και το ποσοστό των ακέραιων πολλαπλασίων του 7 είναι:", count7 * 100, "%.")
else:
    for j in decimal_array:
        integer_multiple(j)
    print("Το ποσοστό των ζυγών είναι:", (count2 / len(decimal_array)) * 100, "% , το ποσοστό των ακέραιων πολλαπλάσιων του 3 είναι:", (count3 / len(decimal_array)) * 100, "%, το ποσοστό των ακέραιων πολλαπλασίων του 5 είναι:", (count5 / len(decimal_array)) * 100, "% και το ποσοστό των ακέραιων πολλαπλασίων του 7 είναι:", (count7 / len(decimal_array)) * 100, "%.")
