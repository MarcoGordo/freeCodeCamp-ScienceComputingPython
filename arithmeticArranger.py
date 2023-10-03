# Aritmetic Arranger

def arithmetic_arranger(problems):
    base_line = ''
    if(len(problems)) > 5:
        return 'Error: Too many problems.'
    arranged_problems = [problems[0], problems[1], problems[2]] 
    firstProblem = problems[0].split()
    print(firstProblem)
    if(len(firstProblem[0]) >= len(firstProblem[2])):
        for char in ' ' + firstProblem[0] : 
            base_line += '-'
    else:
        for char in ' ' + firstProblem[2] : 
            base_line += '-'    
    arranged_problem  = ' ' + firstProblem[0] + '\n' + firstProblem[1] + ' ' + firstProblem[2] + '\n' + base_line
    print(arranged_problem)
    return arranged_problems 
print(arithmetic_arranger(['235 + 52','11 + 3' , '5 + 1002']))
