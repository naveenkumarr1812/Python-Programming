# logical operators (and,or,not) = used to check if two or more statement is true or false

temperature = int(input("What is the temperature outside?: "))

if not(temperature >=0 and temperature <30):
    print("the temperature is good today!")
    print("go outside!")
elif not(temperature < 0 or temperature > 30):
    print("the temperature is bad today!")
    print("stay inside!")