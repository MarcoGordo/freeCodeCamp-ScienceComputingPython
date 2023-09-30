# Aritmetic Arranger

def arithmetic_arranger(arrayOfOps, myBool):
    operations = ['+', '-']
    part1 = ''
    part2 = ''
    leosona = ''
    line = ''
    whiteSpaces = 1
    i = 0
    mySignal = True
    formatArray = []
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
    for char in  ' ' + part1 :
        line += '-'
    toPrint = ' ' + part1 + '\n' + leosona + part2 + '\n' + line     
    if myBool == True :
        toPrint += '\n' + ' ' + str(eval(arrayOfOps[0][0:len(arrayOfOps)-2]))
        formatArray.append(toPrint)
    else:
        formatArray.append(toPrint)    
    return print(formatArray[0])
        
print(arithmetic_arranger(['235 + 52'], True))
