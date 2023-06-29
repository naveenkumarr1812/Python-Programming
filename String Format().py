# str.format() = optional method that gives users
#                more control when displaying output

# Example_1
# animal = "cow"
# item = "moon"
#
# # print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal,item))
# print("The {0} jumped over the {1}".format(animal,item))  #positional argument
# print(f"The {animal} jumped over the {item}".format(animal="cow",item="moon"))  #keyword argument
#
# text = "The {} jumped over the {}"
# print(text.format(animal,item))



# Example_2
# name = "Bro"
#
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))



# Example_3
# number = 10000
# pi = 2.14159

# print("The number pi is {:.3f}".format(pi))  #print after third decimal values
# print("The number is {:,}".format(number))   #Comma after three digit from right
# print("The number is {:b}".format(number))   #In binary format
# print("The number is {:o}".format(number))   #In octal format
# print("The number is {:X}".format(number))   #In Hexadecimal format
# print("The number is {:E}".format(number))   #In Scientific Notation



