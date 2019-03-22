#Exercise- 1 Write a Python program to write a text file "lines.txt" with 100 lines

# Wrinting 100 lines to Lines.txt file
fo = open("lines.txt","w")
for value in range(1,101):
    string = "this is line : "+str(value)+ "\n"
    fo.write(string)
fo.close()



#Exercise- 2 Write a Python program to read and print first 10 lines, lines
# from 50-60 and last 10 lines of the above text file

#read different lines from file
fo = open("lines.txt","r")
counter = 0
for value in fo:
    if counter >= 0 and counter < 10:
        print(value, end= "")
        counter += 1
    elif counter >=50 and counter < 60:
        print(value, end = "")
        counter += 1
    elif counter >= 90 and counter < 100:
        print(value, end = "")
        counter += 1
    else:
        counter += 1
        pass
fo.close()


#Exercise - 3 Write a Python program to append text to above file add 20 more lines into files

# append 20 more line in the end of file
fo = open("lines.txt","a+")
fo.seek(0,2)
for value in range(101,121):
    string = "this is line : "+str(value) + "\n"
    fo.write(string)
fo.seek(0,0)
print(fo.read())
fo.close()



#Exercise  4 Write a Python program to read above created "lines.txt" this file
# will have 120 lines, now we need to read 10 lines and create a new file for 
#these 10 lines, again read next 10 lines and create a new file. continue 
#this till you create 12 files with 10 different lines from "lines.txt"


# create different files from current file
with open("lines.txt","r+") as rf:
    for value in range(1,13):
        name = "lines_"+str(value)
        with open(name,"w+") as wf:
            for i in range(10):
                string = rf.readline()
                wf.write(string)




















