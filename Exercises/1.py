import datetime

name = input("Enter your name \n")
age = int(input("Enter your age \n"))

currentYear = datetime.datetime.now().year

times = int(input("Enter your favourite number\n"))


for i in range(times):
    print("Hi %s, You will be 100 in %d" % (name,currentYear - age + 100))