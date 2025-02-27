from sys import get_int_max_str_digits

import random

def function1():
    number = input("Please enter an 11-digit number: ")
    if not number.isdigit():
        print("The number you enter must consist of numbers")
    elif not len(number) ==11:
        print("You must enter an 11-digit number")
    else:
        inverse_num(number)

def inverse_num(number):
    if number == number[::-1]:
        first_last_digit(number)
    else:
        print("Your number has 11 digits but is not palindromic")
        function1()

def first_last_digit(number):
    if number[0] == "0" and number[-1] == "0":
        print("First and last digit can't be '0'")
        function1()
    else:
        verification_check(number)

def verification_check(number):
    Process1= sum(int(number[i]) for i in [0,2,4,6,8]) *7
    Process2= sum(int(number[i]) for i in [1,3,5,7])
    Process3= (Process1-Process2)
    if Process3 % 10 == 0:
        second_check(number)
    else:
        print("Your number is not suitable for palindromicity and ID")
        function1()

def second_check(number):
    variable= 0
    for i in range(10):
        variable += int(number[i])
    if variable%10  == number[10]%10:
        print("Yes,this number is a valid Turkish ID number and palindrome.")
    else:
        function1()

#FUNCTİON 2
def function2():
    nums = []
    for i in range(5):
        nums.append(random_numbers())
    print(nums)

    tc_numbers = []
    for _ in range(5):
        tc_numbers.append(random_ID())
    print("Generated Turkish ID numbers: \n",tc_numbers)








def random_numbers():

    num= random.randint(10000,99999)
    mid_num=random.randint(0,9) #

    # print("Generated palindromic numbers: \n", num)
    return int(str(num) + str(mid_num) + str(num)[::-1])


def random_ID():
    tcid=[random.randint(1,9)] #First digit can't be 0
    for _ in range(8):
        tcid.append(random.randint(0,9))

    #odd even calculation
    odd= sum(tcid[i] for i in range(0, 9, 2))
    even= sum(tcid[i] for i in range(1, 8, 2))
    tcid.append(((odd * 7) - even) % 10)

    #third provision requirement
    tcid.append(sum(tcid[:10])% 10)

    tc_number = "".join([str(num) for num in tcid])

    return tc_number




if __name__ == "__main__":
    ChooseAnOption= input("Type 1 to find out if the numbers you entered are palindromic and ID number compatible"
                          "\nType 2 to see numbers that are palindromic and conform to TC in mixed form"
                          "\nInput : ")

    if ChooseAnOption == "1":
        function1()
    elif ChooseAnOption == "2":
        function2()
    else:
        print("Please make a valid choice")









