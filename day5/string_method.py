# Capitalize()
m="hello world"
print(m.capitalize()) #Hello world ie first letter lai matra capitalize 

result=m.capitalize()
print(result)

# title()
print(m.title()) #Hello World

# upper()
print(m.upper())

# lower()
print(m.lower())

# split()
m="hello world. i am learning python"
result=m.split() # calling split without any parameter. it splits with space by default
print(result) # "hello", "world", ".", "i", "am", "learning","python"

print(m.split("o")) # o vetne bitikai split garxa ra o lai hatauxa  
['hell', ' w', 'rld. i am learning pyth', 'n']

m="hello, world, i, am, learning, python"
print(m.split(","))


# join()
info=["hello","world","i","am","learning","python"]
result=" ".join(info)  #join the strings wtih space
print(result)
## info.join(" ") should be used as it raises error

print("+".join(info))
print(", ".join(info))

# find() 
m="hello world"
print(m.find("w")) #gives the index of w
print(m.find("rld")) #8
print(m.find("Rld")) # -1 bcuz no R in string so error -1
print(m.find("re")) #error -1 ie no index
# if string is not found then find( ) returns -1

search="Rld"
print(m.find(search.lower()))
print(m.lower().find(search.lower()))

# Replace method .replace(old,new_value)
m="hello world" 
result=m.replace("hello","Hello") #agadi ko purano value paxadi ko naya value
print(result)


