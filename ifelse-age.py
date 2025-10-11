age = input("please enter your age: ")
age = int(age)
if age >= 18:
    print("your age is", age)
    print("you are an adult!")
elif age >= 6:
    print("your age is", age)
    print("you are a teenager!")
else:
    print("your age is", age)
    print("you are a kid!")
