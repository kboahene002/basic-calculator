# #Type conversion into an integer
# import re as regex
#
# print(int('45'))
#
# calc =int(input('Enter a number: '))
# print(type(calc))
#
# print("23" + "22")
#
# #String
# # 1. Escaping characters
# sentence = 'don\'t do that ever'
# print(sentence)
# sentence = "she said \"i want this\" "
# print(sentence)
# #Splitting strings
#
# names = "kelvin,Tracy,Ethel"
#
# tense = "my name is "
#
# for name in names.split(','):
#     print(tense + name)
#
# #Dictionaries
# person = {
#     'name': "kelvin Boahene",
#     'age': 23,
#     'city': "New York",
#     'state': "NY"
# }
# print("I am " + str(person['age']) + " years old")
#
# Built-in functions
# numbers = [15, 2, 32, 4, 5]
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))
# print(len(numbers))
#
# bool("True")
#
# #functions
# def addTwoNumbers(num1, num2):
#     return num1 + num2
#
# print(addTwoNumbers(1, 2))
#
# #one or more parameters
#
# def names_of_people(*names):
#     for my_name in names:
#         print("my name is", my_name)
#
#
# names_of_people(["Kelvin", "Tracy", "Ethel"])
#
# #Rugular Expression
#
# string = "'THIS IS A STRING' she said, Knowing perfectly well it is"
#
# new_string = regex.sub('[^A-Z\'+" "]', '@', string)
# print(new_string)


# Calculator
selector = 0
isTrue = True


def intro():
    print("Welcome to Python Calculator \n 1. Add numbers  \n 2.Multiply numbers \n 3. Divide numbers \n 4. Exit")
    global selector, isTrue
    selector = input("Kindly select an option: ")
    isTrue = True
    selector = int(selector)


def add_numbers(first, second):

    num1 = int(input("Enter the first number: ")) if first is None else first
    num2 = int(input("Enter the second number: ")) if second is None else second
    inner_result = num1 + num2
    print(inner_result)
    question = input("Do you want to add another number to " + str(inner_result) + ":")
    if question == "yes":
        add_numbers(inner_result, None)
    elif question == "no":
        print("Thank you for using this program")
        global isTrue
        isTrue = False
        intro()


def multiply_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    inner_result = num1 * num2
    print(inner_result)
    question = input("Do you want to add another number to the total?")
    if question == "yes":
        multiply_numbers()
    elif question == "no":
        print("Thank you for using this program")
        global isTrue
        isTrue = False
        intro()


def divide_numbers():
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    inner_result = num1 / num2
    print(inner_result)
    question = input("Do you want to perform another operation?")
    if question == "yes":
        divide_numbers()
    elif question == "no":
        print("Thank you for using this program")
        global isTrue
        isTrue = False
        intro()


intro()
if selector == 1:
    while isTrue:
        add_numbers(None, None)
elif selector == 2:
    while isTrue:
        multiply_numbers()
elif selector == 3:
    while isTrue:
        divide_numbers()
elif selector == 4:
    print("Thank you for using this program")
