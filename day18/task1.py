# 1. take 2 numbers as input and add those numbers. Handle the possible exception
try:
    num1=int(input("enter 1st number:"))
    num2=int(input("enter 2nd number:"))

except ValueError:
    print("enter a valid number.")

else:
    print(f"add:{num1+num2}")


# 2. take 2 numbers and a divide. Handle possible exceptions
try:
    num1=int(input("enter 1st number:"))
    num2=int(input("enter 2nd number:"))

except ValueError:
    print("enter a valid number.")

except ZeroDivisionError:
    print("enter non zero number.")

else:
    print(f"division:{num1/num2}")


# 3. create a dictionary student with id, name,age,department. 
# Take a input from the user, which info (id,name,age or department) he want to accesss and print the result. 
# handle the possible exception
student={"id":1234, "name":"aa", "age":20, "department":"Csit"}
try:
    i=input("enter a key:")
    student[i]

except (ValueError, KeyError):
    print("enter a valid key")

else:
    print(f"value:{student[i]}")

