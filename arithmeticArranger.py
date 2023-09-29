# Aritmetic Arranger

def arithmetic_arranger(arrayOfOps, myBool):
    operations = ['+', '-', '*', '/']
    part1 = ''
    part2 = ''
    leosona = ''
    whiteSpaces = 1
    i = 0
    mySignal = True
    #spliting the strings
    for element in arrayOfOps:
        for char in element:
            if char.isnumeric() and mySignal:
                part1 += char
            elif char in operations:
                leosona = char
                mySignal = False
            elif char.isnumeric() and not mySignal:
                part2 += char
    # Adding the Format            
    whiteSpaces = abs(len(part1) - len(part2))           
    if len(part1) > len(part2):
        while(i < whiteSpaces):
            part2 = ' ' + part2  
            i +=1
    else:
        while(i < whiteSpaces):
            part1 = ' ' + part1  
            i += 1                  
    toPrint = [ ' ' + part1 , leosona + part2]
    for element in toPrint:
        print(element)
    for char in toPrint[1] :
        print('-' , end='')
    print()
    if myBool == True :
        print(' ' + str(eval(arrayOfOps[0][0:len(arrayOfOps)-2])))
        
        
arithmetic_arranger(['4505 * 26'], False)
