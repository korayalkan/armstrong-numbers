# Python Algorithms
# Armstrong Numbers

#  Main function
def find_armstrong():

    # User input in this list
    userinput_list = []

    # Power of user_input numbers
    power_list = []

    # Take user input here
    user_input = int(input('Enter a number: '))

    # Length of user input to use when taking power
    # (type: 'int')
    power_number = len(str(user_input))

    # Put user input in the list as a string
    userinput_list.append(str(user_input))

    # For loops to loop through the input list
    for number in userinput_list:
        for num in number:
            # Take the power of the numbers according to the digits
            new_numbers = int(num) ** power_number
            power_list.append(new_numbers)      # Append it to the list

    # Take the sum of the list
    # (type: 'int')
    sum_of_numbers = sum(power_list)

    # Check if the number is an Armstrong Number or not
    if user_input == sum_of_numbers:
        print(f'{user_input} is an Armstrong Number!\n')

    else:
        print(f'{user_input} is not an Armstrong Number!\n')



find_armstrong()
