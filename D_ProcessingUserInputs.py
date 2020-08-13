#function with user input

def CheckWeather(input):
  if input == 1 :
    print("1 was selected")
  elif input == 2:
    print("2 was selected")
  else:
    print("it was above 2")

#>> Convert to float() if requirement is decimals 
inputvariable = int(input("Please enter a number: "))
CheckWeather(inputvariable)

#String formatting

takeInput = input("What is your name: ")
print("Hello %s!" % takeInput.upper())
#>> OR
print(f"Hello {takeInput.upper()}!")
#>> Multiple inputs in a string 

FirstName = input("Whats your first Name:")
MiddleName = input("Whats your middle Name:")
LastName = input("Whats your last Name:")
FamilyName = input("Whats your family Name:")

print("Hello %s %s %s %s" % (FirstName , MiddleName ,  LastName , FamilyName))