#small program 
userInputs = ''
currentInput = ''

while True:
  currentInput = input("Say Something ! ").capitalize()
  if currentInput != "\end":    
    userInputs =  userInputs + " " + currentInput    
    continue
  else:
    print(userInputs)
    break
