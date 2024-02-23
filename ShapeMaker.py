def boxShape(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"Symbol" need to be a string of 1.')
    
    width = int(width)
    height = int(height)

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

symbol = input("Enter your symbol: ")
print("You have choosen " + symbol)
width = input("Enter your width: ")
print("You have choosen " + width)
height = input("Enter your height: ")
print("You have choosen " + height)

boxShape(symbol, width, height)


