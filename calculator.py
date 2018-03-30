import re

print("Our Magical Calculator")
print("type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if equation == 0:
        equation = input("enter equation:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye Gabi")
        run = False
    else:
        inputValue = equation
        try:
            equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

            if previous == 0:
                previous = eval(equation)
            else:
                previous = eval(str(previous) + equation)

            #print("you type", previous)

        except:
            print("Has invalid chars:", inputValue)



while run:
    performMath()