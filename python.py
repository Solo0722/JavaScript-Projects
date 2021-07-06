news ="hello world"
print(news.upper())

a="hello dear"
b="what is your name?"
c=a +" "+b
print(c.title())


#numbers
print(2.5+3.4)
print(3**3)
print(18/3)


#upper and lower method
print((2+3)*6)
bicycles=["trek","bmw"]
print(bicycles[1].upper())

#title() method
bicycles=["trek","bmw"]
news ="my first bicycle was a " +bicycles[1].title()+ "."
print(news)

#how to select an item from a list
bicycles=["trek","bmw"]
bicycles[0]="suzuki"
print(bicycles)


#append() method
bicycles=["trek","bmw"]
bicycles.append("suzuki")
print(bicycles)



#insert() method
bicycles=["trek","bmw"]
bicycles.insert(1,"kia")
bicycles.append("suzuki")
print(bicycles)


#del method
bicycles=["trek","bmw"]
del bicycles[0]
print(bicycles)

#pop() method
names=["ama","solo","aba","anita","vero","fire"]
print(names)
popped_names=names.pop()
print(names)
print(popped_names)
news="my first name is "+popped_names.title()+" ."
print(news)

names=["ama","solo","aba","anita","vero","fire"]
names.pop(0)
print(names)

#remove() method
names=["ama","solo","aba","anita","vero","fire"]
expensive="solo"
names.remove(expensive)
print(names)
print(expensive)


#how to sort items permanently
names=["ama","solo","aba","anita","vero","fire"]
names.pop(1)
names.sort()
print(names)

names=["ama","solo","aba","anita","vero","fire"]
names.sort(reverse=True)
print(names)
print(names)

#how to sort items temporarily
names=["ama","solo","aba","anita","vero","fire"]
print(sorted(names))
print(names)


#how to print a list in reverse order:this reverses the order of the list
names=["ama","solo","aba","anita","vero","fire"]
names.reverse()
print(names)

#how to find the length of a list
cars =["audi","kia","toyota"]
len (cars)
print(len(cars))

#how to access the last item in a lists
print(cars[-1])

#looping through an entire list using the for loop
subjects=["Maths","English","Science","Biology"]
for a in subjects:
   print(a.upper()+ " is my favourite subject.")
   print(a.title()+ " is also the most difficult subject." "\n")

print("I like all the subjects we do in class")

#making numerical lists
for value in range(1,6):
	print(value)

#using range to create a list of numbers
numbers=list(range(0,6))
print(numbers)

numbers=list(range(2,11,2))
print(numbers)

squares=[]
for value in range(1,11):
	square=value**2;
	squares.append(square)
print(squares)

squares=[]
for value in range(1,11):
	squares.append(value**3)
print(squares)


#others uses of list of numbers
numbers=list(range(1,20))
print(min(numbers))

numbers=list(range(1,20))
print(max(numbers))

numbers=list(range(1,20))
print(sum(numbers))

#list comprehension
squares=[3*(value+2) for value in range(1,11)]
print(squares)

#slicing a list
names=["Ama","Aba","Solo","Anita","Vero","Fire"]
print(names[-3:])


#looping through a slice
names=["Ama","Aba","Solo","Anita","Vero","Fire"]
for name in names[0:3]:
	print(name+ " is my sibling")


#copying a list
my_fruits=["orange","mango","pear","watermelon"]
sisters_fruits=my_fruits[:]
print("My favourite fruits are:")
print(my_fruits)
print("\n""My sister's favourite fruits are:")
print(sisters_fruits)


#tuples:they are list that cannot change
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
print(dimensions)


#if statements
names=["Ama","Aba","Solo","Anita","Vero","Fire"]
for name in names:
	if name=="Solo":
		print(name.upper())
	else:
		print(name.title())


car="audi"
print(car!="audi")

cars="audi"
if cars != "chvrolet":
	print("This is not my car. My car is " +car)
else:
	print("This is my car")

#numerical comparisons
#to check if a staement is true or false
age=19
print(age<21)

age=19
print(age<=21)

age=19
print(age>21)

#checking multiple conditions using "and"
number_1=5
number_2=7
print(number_1<6 and number_2<10)

number_1=5
number_2=7
print(number_1>6) and (number_2<=10)
print(number_1>6 and number_2<=10)

#checking multiple statements using "or"

age_1=5
age_2=19
print(age_1>10 or age_2>10)

print("\n")
#checking whether a value is in a list
names=["Ama","Aba","Solo","Anita","Vero","Fire"]
print("Aba" in names)

names=["Ama","Aba","Solo","Anita","Vero","Fire"]
print("Owusu" in names)

#checking whether a value is not in a list
names=["Ama","Aba","Solo","Anita","Vero","Fire"]
print("Aba" not in names)
print("Owusu" not in names)

names=["Ama","Aba","Solo","Anita","Vero","Fire"]
name="Owusu"
if "Owusu" not in names:
		print("Owusu is not in the list")


#if-else statements
print("\n")
age=19
if age>=18:
	print("You are old enough to vote!")
else:
	print("Sorry, you are too young to vote.")


#if-elif-else chain
print("\n")
age=2
if age< 4:
	print("Your admission fee is free!")
elif age<18:
	print("Your admission fee is 5 dollars. ")
elif age>=18:
	print("Your admission fee is 10 dollars.")


age=12
if age< 4:
	price=0
elif age<18:
	price=5
elif age>=18:
	price=10
print("Your admission cost is $"+str(price))

#using if statements with lists
names=["Ama","Aba","Solo","Anita","Vero","Fire"]
for name in names:
	if name=="Solo":
		print("Sorry you can not enter "+name)
	else:
		print("You are welcome! "+name)

#checking that a list is not empty
print("\n")
names=[]
if names:
	for name in names:
		print("You are welcome! "+name)
else:
	print("Nobody wants to come to the party.")

#using multiple lists
print("\n")
available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding "+requested_topping)
	else:
		print("Sorry we do not have "+requested_topping)




#DICTIONARIES
print("\n")
alien_0={"color":"blue","points":5}
print(alien_0["color"])
print(alien_0["points"])

alien_0={"color":"blue","points":5}
new_points=alien_0["points"]
print("You just earned "+str(new_points)+ " points")

#adding new key-value pairs
alien_0={"color":"blue","points":5}
print(alien_0)
alien_0["x-position"]=0
alien_0["y-postion"]=25
print(alien_0)

#starting with empty dictionaries
alien_0={}
alien_0["color"]="blue"
alien_0["points"]=5
print(alien_0)

#modifying values in dictionaries
alien_0={"color":"blue","points":5}
print(alien_0)
alien_0["color"]="black"
print(alien_0)



alien_0={"x-position":0,"y-position":25,"speed":"slow"}
print("Original x-position: "+str(alien_0["x-position"]))

if alien_0["speed"]=="slow":
	x_increment=1
elif alien_0["speed"]=="medium":
	x_increment=2
elif alien_0["speed"]=="fast":
	x_increment=3

alien_0["x-position"]=alien_0["x-position"]+x_increment
print("New x-position: "+str(alien_0["x-position"]))


#removing key-value pairs
alien_0={"color":"blue","points":5}
del alien_0["color"]
print(alien_0)

#dictionary of similar objects

favourite_languages={
	"Solomon":"Javascript",
	"Elikem":"Python",
	"Jesse":"Ruby",
	"Jahnissi":"Java",
	"Benedict":"Pearl"
	}
print("Elikem's favourite programming language is: "+favourite_languages["Elikem"])


#looping through a dictionary
#looping through all key-value pairs
user={
	"first":"Solomon",
	"last":"Owusu",
	"age":"nineteen"
	}
for data,value in user.items():
	print("\n Data: "+data)
	print("Value: "+value)

favourite_languages={
	"Solomon":"Javascript",
	"Elikem":"Python",
	"Jesse":"Ruby",
	"Jahnissi":"Java",
	"Benedict":"Pearl"
	}
for name,language in favourite_languages.items():
	print("\n" +name.title()+"'s favourite programming language is "+language.title())


#looping through only the keys in a dictionary
favourite_languages={
	"Solomon":"Javascript",
	"Elikem":"Python",
	"Jesse":"Ruby",
	"Jahnissi":"Java",
	"Benedict":"Pearl"
	}
for name in favourite_languages.keys():
	print("\n"+name)


favourite_languages={
	"Solomon":"Javascript",
	"Elikem":"Python",
	"Jesse":"Ruby",
	"Jahnissi":"Java",
	"Benedict":"Pearl"
	}
friends=["Elikem","Jesse"]
for name in favourite_languages.keys():
	print(name.title())

	if name in friends:
		print("Hi "+name+ " I see your favourite programming language is "
		 +favourite_languages[name])

#looping through all values in a dictionary
favourite_languages={
	"Solomon":"Javascript",
	"Elikem":"Python",
	"Jesse":"Ruby",
	"Jahnissi":"Java",
	"Benedict":"Python"
	}
for value in set(favourite_languages.values()):
	print(value)
#If the keys or values appear more than one and you want to chose each of them, 
#use set()


#NESTING
#nesting a set of dictionary in a list example 1
alien_0={"color":"black","points":5}
alien_1={"color":"blue","points":10}
alien_2={"color":"yellow","points":15}

aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)

#example 2
alien_0={"color":"black","points":5}
alien_1={"color":"blue","points":10}
alien_2={"color":"yellow","points":15}

aliens=[alien_0,alien_1,alien_2]
print(aliens)

#using range()-example 3
print("\n")
aliens=[]
for alien_number in range(0,30):
	new_alien={"color":"blue","points":10}
	aliens.append(new_alien)
for alien in aliens[3:5]:
	if alien["color"]=="blue":
		alien["color"]="yellow"
		alien["points"]=20
		print(alien)
for alien in aliens[:10]:
	print(alien)


#nesting a list in a dictionary
pizza={
	"crust":"thick",
	"toppings":["mushrooms","extra cheese"]
	}
print("You ordered a "+pizza["crust"]+ "-crust pizza with the following toppings: ")
for topping in pizza["toppings"]:
	print("\t"+topping)

#nesting a list in a dictionary example 2
favourite_languages={
	"Solomon":["Javascript","Python"],
	"Elikem":["Python","Pearl"],
	"Jesse":["Ruby"],
	"Jahnissi":["Java","Ruby"],
	"Benedict":["Python"]
	}
for name,languages in favourite_languages.items():
	print("\n"+name.title()+ "'s favourite languages are:")
	for language in languages:
		print(language)


#nesting a dictionary in a dictionary
users={
	"sowusu":{
	"first":"Solomon",
	"last":"Owusu-Ansah",
	"location":"Kumasi"
		},
	"aeinstein":{
	"first":"Albert",
	"last":"Einstein",
	"location":"New York"
		}
}
for user_name,user_info in users.items():
	print("\nUsername: "+user_name)
	full=user_info["first"]+" "+user_info["last"]
	location=user_info["location"]
	print("Full name: "+full)
	print("Location: "+location)



#USER INPUT AND WHILE LOOPS
"""message=input("Tell me something and i will repeat it to you:")
print(message)

name=input("Please enter your name: ")
print("Hello "+name)

#using prompt
user="If you tell us more about you, we can personalize your information"
user +="\nWhat is your name?"
name=input(user)
print("Hello "+name+ "!")


#whlie loop
current_number =1
while current_number<=5:
	print(current_number)
	current_number+=1

#letting the user choose when to quit
prompt="Tell me something and I will repeat it to you:"
prompt+="\nEnter when to quit the program"

message=""
while message != "quit":
	message=input(prompt)
	print(message)

#using int() to accept numerical input
age=input("How old are you?")
print(int(age))

height=input("How tall are you?")
height=int(height)

if height >=36:
	print("You are tall enough to ride")
else:
	print("you cannot ride please")


#using the modulo operator
message=input("Tell me a number and I will tel you whether it is even or odd:")
message=int(message)

if message%2==0:
	print("this number is an even number")
else:
	print("this number is an odd number")

#letting the user choose when to quit
message=input("Tell me when to quit:")
while message !="quit":
	print(message)
"""
	


#FUNCTIONS
def greet_user():
	print("Hello world")
greet_user()

#passing an information to the function
def greet_user(username):
	print("Hello "+username.title())
greet_user("solomon")
	
'''	
#using flag
prompt="Tell me something and I will repeat it to you: "
prompt +="\nEnter 'quit' to end the program"

active =True
while active:
	message=input(prompt)
	if message=="quit":
		active=False
	else:
		print(message)

#using break to exit a loop

prompt="Tell me something and I will repeat it to you: "
prompt +="\nEnter 'quit' to end the program"
while True :
	city=input(prompt)
	if city=="quit":
		break
	else:
		print("I'd love to go to "+city.title()+" !")
	'''
	
#using continue in a loop
current_number=0
while current_number <10:
	current_number+=1
	if current_number%2==1:
		continue
	else:
		print(str(current_number))
print("\n")


#using while loops in lists and dictionaries
#moving items from a list to another
unconfirmed_users=["Alice","Solomon","Eric","Maxwell"]
confirmed_users=[]

while unconfirmed_users:
	current_users=unconfirmed_users.pop()
	print("Verifying user: "+current_users.title())
	confirmed_users.append(current_users)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())



#removing all instances of specific values from a list
pets=["cats","hen","snake","cats","dogs","dogs","cow","rabbit"]
print(pets)
while "cats" in pets:
	pets.remove("cats")
while "dogs" in pets:
	pets.remove("dogs")
print(pets)


'''
#filling a dictionary with user input
reponses={}

polling_active=True
while polling_active:
	name=input("\nWhat is your name?")
	reponse=input("Which mountain would you like to climb oneday?")

	reponses[name]=reponse
	repeat=input("Would you like to let another person respond?(yes/no)")
	if repeat=="no":
		polling_active=False

print("\n---Polling Results----")
for name,response in reponses.items():
	print(name+ " would like to climb "+reponse+".")

'''

#FUNCTIONS
#Defining functions
def sayhello():
	print("Hello")
sayhello()

#passing information to the function
def sayhello(username):
	print("Hello "+username.title())
sayhello("Solomon")


#multiple function calls
def describe(username,age,hobby,):
	print(username.title()+" is "+str(age)+ " years old.")
	print(username.title()+ "'s hobby is "+hobby+ ".")
describe("Solomon",19,"playing football\n")
describe("ama",15,"playing Ampe")
	
	
def describe(username,age,hobby,):
	print(username.title()+" is "+str(age)+ " years old.")
	print(username.title()+ "'s hobby is "+hobby+ ".")
describe(username="Solomon",age=19,hobby="playing football\n")
describe(age=15,hobby="playing Ampe",username="ama")
	
def describe(pet_name,animal_type="dog"):
	print("\nI have a "+animal_type+".")
	print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe("peace")	


#returning a simple value
def name(first,last):
	full=first+" "+last
	return full
print(name("Solomon","Owusu"))

#making an argument optional
def name(first,last,middle=""):
	if middle:
		full=first+" "+middle+" "+last
	else:
		full=first+" "+last
	return full
print(name("Solomon","Owusu","Ansah"))
print(name("Elikem","Anyomi"))


#returning a dictionary
def person(first,last):
	name={"first":first,"last":last}
	return name
print(person("Jahnissi","Asante"))


#extending a dictionary in a function
def build_person(first,last,age=""):
	person={"First name":first,"Last name":last}
	if age:
		person["age"]=age
	return person
print(build_person("Jesse","Asante",18))

'''
#using a function with a while loop
def get_formatted_name(first,last):
	full=first+" "+last
	return full.title()
while True:
		print("\nPlease telll me your name:")
		f_name=input("First name:")
		l_name=input("Last name:")
		formatted_name=get_formatted_name(f_name,l_name)
		print("\nHello, "+formatted_name+"!")


def get_formatted_name(first,last):
	full=first+" "+last
	return full.title()

while True:
		print("\nPlease tell me your name:")
		print("Enter 'quit' to exit")

		f_name=input("First name: ")
		if f_name=="quit":
			break
		l_name=input("Last name: ")
		if l_name=="quit":
			break
formatted_name=get_formatted_name(f_name,l_name)
'''

#passing a list
def sayhi(names):
	for name in names:
		print("Hello, "+name+"!")
usernames=["Abigail","Olivia","Sussana","Augustina"]
sayhi(usernames)

#modifying a list in a function
unprinted_designs=["robot","cars","pentagon"]
printed_designs=[]
while unprinted_designs:
	current_designs=unprinted_designs.pop()
	print("Printing design: "+current_designs)
	printed_designs.append(current_designs)
print("The following have been printed out: ")
for printed_design in printed_designs:
	print(printed_design)


#passing an arbitrary number of arguments
def make_pizza(*toppings):
	print(toppings)
make_pizza("pepperoni")
make_pizza("mushrooms")

def make_pizza(*toppings):
	print("\nMaking a pizza with the following toppings: ")
	for topping in toppings:
		print("-"+topping)
make_pizza("mushrooms","pepper","tomatoes")
	



	
	
	
	
	
	
	
	
	
	
	
