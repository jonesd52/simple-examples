# Render a simple ASCII-art tree, with a centered base
#
# Console input should be of the format (int) (char) (char)
# the int should be odd numbered, and between 3 and 21.  The first char is
# the base of the tree.  The second char is the rest of the tree.

global userInput

def buildTree(theInput):
    theInput = theInput.split(" ")
    width = 1
    while width <= int(theInput[0]):
        spacing = int(int(theInput[0]) / 2 - width / 2)
        print((' ' * spacing) + (theInput[2] * width))
        width += 2

    spacing = int(int(theInput[0]) / 2 - 1)
    print((' ' * spacing) + (theInput[1] * 3))

def repromptInput():
    print "Failed"
    return False

def parseInput(theInput):
    newInput = ""
    newInput = theInput.split(" ")
    if (len(newInput) != 3):
        return repromptInput()
    if not (newInput[0].isdigit()):
        return repromptInput()
    if not (int(newInput[0]) >= 3 and int(newInput[0]) <= 51 and int(newInput[0]) & 1):
        print "Here!"
        return repromptInput()
    if len(newInput[1]) != 1:
        return repromptInput()
    if len(newInput[2]) != 1:
        return repromptInput()
    userInput = newInput
    return True

def main():
    while True:
        userInput = input()
        testInput = parseInput(userInput)
        if (testInput == True):
            break
    buildTree(userInput)

main()
