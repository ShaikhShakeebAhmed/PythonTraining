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