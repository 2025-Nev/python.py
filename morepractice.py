hello_list = ["Hello", "this", "is", "a", "list"]


hello_list = list()
hello_list.append("Hello,")
hello_list.append("this")
hello_list.append("is")
hello_list.append("a")
hello_list.append("list")

print(hello_list[4])
hello_list[4] += "!"
hello_list[4] = hello_list[4] + "!"
print(hello_list[4])
hello_dict ={"first_name": "Nev", "last_name": "Nyamhindu","wealth_status": "rich as fuck"}
print(hello_dict)

#FUNCTIONS
def greet_user():
    """Greeting a user"""
    print("Hello")

greet_user()

def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello,{username.title()}!")

greet_user('nev')
    
def display_message():
    """A simple display message"""
    print("I am learning about functions and it is amazing.")

display_message()

def eating_tacos():
    """Display food I am eating"""
    print("I am eating tacos.")

eating_tacos()

def eating_tacos():
    """Display what I am eating"""
    print("I am eating tacos and avocadoes")

eating_tacos()

def favorite_book():
    """Display my favorite book"""
print("Alice in Wonderland")

favorite_book()

