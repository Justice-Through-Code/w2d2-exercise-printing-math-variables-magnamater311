
# def convert_100_to_celsius():
    # Convert a temperature of 100 degrees fahrenheit to celsius
    # Save this to a variable called celsius_100, and use print() to print out the value
celsius_100 = 100
print ((celsius_100 - 32) * 5/9 )

# *** I got a float. I know this because of the decimal***


    # Is the resulting temperature you get an integer or float? 
    # Print 'float' if it is a float or 'int' if it is an int
    # How do you know? Write a comment below your code explaining how you know which it is

# convert_100_to_celsius()

# def convert_0_to_celsius():
    # Convert a temperature of 0 degrees fahrenheit to celsius
    # Save this to a variable called celsius_0, and use print() to print out the value
print((0 - 32) * 5/8)

#convert_0_to_celsius()

# def convert_34_2_to_celsius():
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    # Do this one all in one print statement without saving any variables
print ((32.2 - 32) * 5/9)
    
#convert_34_2_to_celsius()


# Now, can you convert back?
print ((0.11 + 32) * 5/9)


# def convert_5_to_fahrenheit():
    # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
print ((5 - 32) * 5/9)

#convert_5_to_fahrenheit()

#def hotter_temp():
    # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively


# hotter_temp()
def hotter_temp():
    celsius_temp = 30.2
    fahrenheit_temp = 85.1
    
    if celsius_temp > (fahrenheit_temp - 32) * 5/9:
        print(f"{celsius_temp} degrees celsius")
    else:
        print(f"{fahrenheit_temp} degrees fahrenheit")

hotter_temp()
