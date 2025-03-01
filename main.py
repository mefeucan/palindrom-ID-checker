from sys import get_int_max_str_digits

import random

def number_feedback():
    """Receives and validates an 11-digit number from the user.

    Checks that the value entered by the user consists of digits and has 11 digits.Gives an error message
     if it is not a valid input value and prompts to enter the value again.

    If the input is valid, it calls the 'inverse_num' function which inverts the number.
    """

    number = input("Please enter an 11-digit number: ")
    if not number.isdigit():
        print("The number you enter must consist of numbers")
    elif not len(number) == 11:
        print("You must enter an 11-digit number")
        number_feedback()
    else:
        inverse_num(number)



def inverse_num(number):
    """Compares the number to its inverse to check if the entered number is palindromic.

    If the result is true, it calls the function 'first_last_digit' which checks the first and last digit of the number.

    If it is incorrect, it gives an error message and calls the 'function1()' function to provide the user with a new login.
    """

    if number == number[::-1]:
        check_first_and_last_digit(number)
    else:
        print("Your number has 11 digits but is not palindromic")
        number_feedback()


def check_first_and_last_digit(number):
    """Checks whether there is 0 in the first and last digits of the number.

    If the first and last digits are 0, it gives an error message and
    allows the user to enter a new value by calling the 'function1()' function.

    If the first and last digits are not 0, the 'verification_check' function is called
     which checks the digits with specific operations.
    """

    if number[0] == "0" and number[-1] == "0":
        print("First and last digit can't be '0'")
        number_feedback()
    else:
        verification_check(number)



def verification_check(number):
    """Sum of the 0th 2nd 4th 6th 8th elements and then multiplies the result by 7.
    Then sum of the 1st 3rd 5th 7th elements and subtracts the second result from the first result.
    Divides the result of subtraction by the number 10.

    If the remainder is equal to 0, it calls the 'second_check' function that checks the digits with certain operations.

    If the remaining number is not 0, it gives an error message and
     gives the user a new login by calling the 'function()' function.
    """

    Process1 = sum(int(number[i]) for i in [0,2,4,6,8]) *7
    Process2 = sum(int(number[i]) for i in [1,3,5,7])
    Process3 = (Process1-Process2)
    if Process3 % 10 == 0:
        second_verification_check(number)
    else:
        print("Your number is not suitable for palindromicity and ID")
        number_feedback()



def second_verification_check(number):
    """Sums the first 10 digits and divides the result by 10.
    Divides the 11th digit by 10

    If the remainders of the result of these two operations are equal, a confirmation message is displayed on the user screen.

    If the results are not equal, it displays an error message and calls the 'function1()' function,
     giving the user the opportunity to enter a new value.
    """

    variable = 0
    for i in range(10):
        variable += int(number[i])
    if variable % 10  == number[10] % 10:
        print("Yes,this number is a valid Turkish ID number and palindrome.")
    else:
        print("The number you entered is not suitable for palindromic and ID")
        number_feedback()




def randomize_numbers():
    """Creates an empty list to store palindromic numbers.
    Generates five palindromic numbers using the function 'random_numbers()'.
    Prints the generated palindromic numbers on the screen.

    Create an empty list to store ID numbers.
    Generates five ID numbers using the function 'random_ID()'.
    Prints the generated ID numbers on the screen.
    """

    nums = []
    for i in range(5):
        nums.append(generate_random_numbers())
    print("Generated palindromic numbers: \n",nums)

    tc_numbers = []
    for _ in range(5):
        tc_numbers.append(generate_random_ID())
    print("Generated Turkish ID numbers: \n",tc_numbers)



def generate_random_numbers():
    """Generates a random number between 10000 and 99999.
    Generates a random digit between 0 and 9 (for the middle digit).
    Combines the generated number, the middle digit and the inverse of the number to form a palindromic number.
    """

    num= random.randint(10000,99999)
    mid_num=random.randint(0,9)
    return int(str(num) + str(mid_num) + str(num)[::-1])



def generate_random_ID():
    """Generates the first digit of the ID number (a random number between 1 and 9).
    Generates digits 2 to 9 of the Turkish ID number (random digits between 0 and 9).

    To fulfill certain conditions:
     Calculates the sum of digits in a single index (1st, 3rd, 5th, 7th, 9th digits).
     Calculates the sum of digits in a double index (2nd, 4th, 6th, 8th digits).

     Calculates the 10th digit: (sum of odd digits * 7 - sum of even digits) mod.
     Calculates the 11th digit: Mod 10 of the sum of the first 10 digits.

     Concatenate TC ID number to string.
     Return the generated ID number.
     """

    tcid=[random.randint(1,9)] #First digit can't be 0
    for _ in range(8):
        tcid.append(random.randint(0,9))

    #10th digit calculation
    odd= sum(tcid[i] for i in range(0, 9, 2))
    even= sum(tcid[i] for i in range(1, 8, 2))
    tcid.append(((odd * 7) - even) % 10)

    #11th digit calculation
    tcid.append(sum(tcid[:10])% 10)

    tc_number = "".join([str(num) for num in tcid])

    return tc_number



if __name__ == "__main__":
    """It displays the options to the user and asks them to make a selection.
    If the user selects 1, it runs 'function1()'.
    If the user selects 2, it runs 'function2()'.
    
    It warns the user if an invalid selection is made."""

    ChooseAnOption= input("Type 1 to find out if the numbers you entered are palindromic and ID number compatible"
                          "\nType 2 to see numbers that are palindromic and conform to TC in mixed form"
                          "\nInput : ")

    if ChooseAnOption == "1":
        number_feedback()
    elif ChooseAnOption == "2":
        randomize_numbers()
    else:
        print("Please make a valid choice")









