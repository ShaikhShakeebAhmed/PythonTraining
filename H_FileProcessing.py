#basic reading a file
#>> better to read the file in to a variable as the cursor moves to the end of the file and running the read again on the same object will not return anything

myFile = open("Additionalfiles/fruits.txt")

alltheFile = myFile.read()

#>> Good idea to close the file
myFile.close()

print(alltheFile)

#>> reading a file using With context manager
with open("Additionalfiles/fruits.txt") as myfile2:
  readmyfile = myfile2.read()

print(readmyfile)

#Writing a file

with open("Additionalfiles/Vegitables.txt" , "w") as writeMyfile:
  writeMyfile.write("artichoke\n aubergine\n asparagus\n broccoflower ")

#Appending to a File
with open("Additionalfiles/Vegitables.txt" , "a") as writeMyfile:
  writeMyfile.write("\n artichoke\n aubergine\n asparagus\n broccoflower ")

#Appending to a File then read at the same time
with open("Additionalfiles/Vegitables.txt" , "a+") as writeMyfile:
  writeMyfile.write("\n artichoke\n aubergine\n asparagus\n broccoflower ")
  writeMyfile.seek(0) #move the cursor to position 0
  readthefile = writeMyfile.read()

print(readthefile)

