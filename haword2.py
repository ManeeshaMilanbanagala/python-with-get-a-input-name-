#split do you wanna get the piece of users name we used that one 
name = input("Whats your name\n").strip().title()
first,last = name.split(" ")
print(f"hello, {first}")