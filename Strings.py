#Python strings
x = "Hello"
print(x)

#Slicing strings
x = "Python"
print(x[0])

x = "Hello, World!"
print(x[1:5])

x = "Hello, World!"
print(x[:4])

x = "Hello, World!"
print(x[1:])

x = "Hello, World!"
print(x[-5:-2])

#Modify strings
x = "Hello"
print(len(x))

x = "Hello, World!"
print(x.upper())

x = "Hello, World!"
print(x.lower())

x = " Hello, World! "
print(x.strip())

x = "Hello, World!"
print(x.split(","))
#Concatenate strings
a = "Hello"
b = "World"
print(a + " " + b)

a = "Hello"
b = "World"
c = a + b
print(c)
#Format strings
age = 12
txt = f"My name is Bob, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)
#Escape characters
print('It\'s a nice day!')

print("This is a backslash: \\")

print("Hello\nWorld")

print("Name\tAge\tCity")

print("12345\rABCDE")
#String methods
print("hello world".capitalize())

print("banana".count("a"))

print("Hello World".find("World"))

print("I like Java".replace("Java", "Python"))

print("-".join(["2026","01","31"]))




