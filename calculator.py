import re as regex
print("OUR MAGICAL CALCULATOR")
print("-"*40)
result = 0
isTrue = True
run = True


def take_input():
    exp = input("Kindly enter the operation:")
    exp = regex.sub('[^0-9-+*/]', "", exp)
    return exp


while run:
    calc = take_input()
    calc = eval(calc)
    print(calc)
    if calc != 0:
        result = calc

    while isTrue:
        answer = input("Do you want to continue?(y/n)")
        if answer == "y":
            isTrue = True
            new_exp = input(result)
            new_string = str(result) + str(new_exp)
            result = eval(new_string)
            print(result)
        elif answer == "n":
            isTrue = False
            print("Thank You")





