
while True:
    num_input = input("Enter your number here:  ")

    if num_input.isnumeric() != True:
        print("Silly goose! Your number must be a positive whole number integer")
    # if int(num_input) < 0:
    #    print("Your number must be greater than 0")
    else:
        print(num_input)
