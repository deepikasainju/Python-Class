filename="message.txt"

# with open(filename, "w") as fp:
#     fp.write("hello world. \n i am learning python")


# read()
# seek()
# readlines()
# tell()
# writelines()

with open(filename, "r") as fp:
    data=fp.read()
    print(data)

    fp.seek(0) # first ma read garda file pointer last sama pugxa so feri first bata read garna seek(0) garne
    data=fp.read(7) # vitra 7 ley kati wota letter read grane vanxa
    print(data)

    fp.seek(0)
    data=fp.readline()
    print(data)

    fp.seek(0)
    data=fp.readlines() #['hello world. \n', ' i am learning python']
    print(data)

data=["hello world \n"," you are fucked up as hell. \n", "well so i am going crazy"]
with open(filename, "w") as fp: # w mode ma jailey overwrite hunxa
    fp.writelines(data)