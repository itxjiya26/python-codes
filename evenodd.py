def check_even_odd(num):
    # Check if num divided by 2 leaves remainder 0
    if (num % 2) == 0:
        print("The number is even")
    else:
        print("The number is odd")

# Take input from user and call the function
number = int(input("Please enter any number: "))
check_even_odd(number)


