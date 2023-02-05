#I am practising coding in python
#First lesson on Variables
message = "Nev is a billionaire"
print(message)
message = "Owns multiple companies around the world"
print(message)
name = "ada lovelace"
print(name.title())
new_name = "KlearSyt"
print(new_name.title())
Companyname = "30-minute Code"
print(Companyname)
name2 = "Ngonidzashe"
print(name2)

#Coding practise ends here
first_name = "ngonidzashe"
last_name = "nyamhindu"
full_name = f"{first_name} {last_name}"
print(full_name.upper())

#Learning strings
message = f"Hello, {first_name} {last_name}"
print(message.upper())

print('Hello World!')
person = input('What\'s your name?')
print('Hello, ', person)
standard_input = 'hello world'

all_number = 25+5/3*3/3
print(all_number)

#Creating a program that follows order of operations
order = 2 + 4 * 3
print(order)

customer_rate = 45 * 150/100
print(customer_rate)
customer_rate2 = 120/100 * 200

pens = 100/100 * 8 - 40/100 * 8
print(pens)

order2 = 25/5+6-15/3*2
print(order2)
 
order3 = 22/5+6+6+4/2
print(order3)

#VARIABLES STORE AND LABEL DATA 
#EXAMPLES OF DATA TYPES
#Integer Stores whole numbers
#Float Stores decimal numbers 
#Boolean Can have a value of True or False
#String Stores a collection of characters. “Hello World” is a string
#List Contains a collection of data in a specific order
#Tuple Contains a collection immutable data in a pecific order
#Dictionary contains mapped data and data is stored in key-value pairs

hello_str = “Hello World”
hello_int = 21
hello_bool = True
hello_tuple = (21, 32)
hello_list = [“Hello,”, “this”, “is”, “a”, “list”]

# This list now contains 5 strings. Notice that there are no spaces
# between these strings so if you were to join them up so make a sentence
# you’d have to add a space between each element.
hello_list = list()
hello_list.append(“Hello,”)
hello_list.append(“this”)
hello_list.append(“is”)
hello_list.append(“a”)
hello_list.append(“list”)
# The first line creates an empty list and the following lines use the append
# function of the list type to add elements to the list. This way of using a
# list isn’t really very useful when working with strings you know of in 
# advance, but it can be useful when working with dynamic data such as user
# input. This list will overwrite the i rst list without any warning as we
# are using the same variable name as the previous list.
hello_dict = { “first_name” : “Liam”,
 “last_name” : “Fraser”,
 “eye_colour” : “Blue” }

 print('Nev is dope')