# Aritmetic Arranger

def arithmetic_arranger(arrayOfOps, myBool):
    operations = ['+', '-', '*', '/']
    part1 = ""
    part2 = ""
    leosona = ""
    mySignal = True
    for element in arrayOfOps:
        for char in element:
            if char.isnumeric() and mySignal:
                part1 += char
            elif char in operations:
                leosona = char
                mySignal = False
            elif char.isnumeric() and not mySignal:
                part2 += char
                mySignal = False  
    print(part1)
    print(leosona)
    print(part2)
    print('ok')

arithmetic_arranger(['45+26'], True)
