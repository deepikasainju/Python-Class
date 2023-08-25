# we can open, close, read, write or perform any other kind of work with file using python
# there are several modes from which we can open a file
# r = read file
# w= write in file
# a= append mode
# r+ = read and write mode
# w+ = write and read mode
# x = exclusive write mode 
# a+ = append and read mode

filename= "message.txt"
fp=open(filename, "w")
fp.write("hello world")
fp.close()

fp=open(filename, "r")
data= fp.read()
print(data)
print(type(data))
fp.close()

# closing the file is important as it protects the system from memory leakage(system slow avoid)
# but sometimes we may forget to open the file
# so it is better to open a file with context manager

with open(filename, "a") as fp: # conetxt manager
    fp.write("\nI am learning python")

with open(filename, "r+") as fp:
    data= fp.read()
    fp.seek(0)# fila ma cursor lai agadi gayera halxa 
    fp.write("python is a high level language") # sabai kura overwrite hunxa 
    # sabai hatera yo write hunxa if cursor is in the first position

with open(filename, "w+") as fp:
    fp.write(" i'm learning")
    fp.seek(0)
    data=fp.read()
    print(data)

# same file feri banna nadina exclusive use garxam
# overwrite huna didaina
with open(filename, "x") as fp:
    fp.write("i am bored")
