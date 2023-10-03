
def arithmetic_arranger(problems , solve = False):
    # First check, Length of the list is almost of five problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    top_line = ''
    middle_line = ''
    bottom_line = ''
    result_line = ''

    for problem in problems:
        firstProblem = problem.split()
        operand1 = firstProblem[0]
        operator = firstProblem[1]
        operand2 = firstProblem[2]

        max_length = max(len(operand1), len(operand2)) + 2
        top_line += operand1.rjust(max_length) + '    '
        middle_line += operator + operand2.rjust(max_length - 1) + '    '
        bottom_line += '-' * max_length + '    '

        if(solve == True):
            try:
                result = str(eval(problem))
                result_line += result.rjust(max_length) + '    '
            except:
                return 'Error: Invalid problem.'

    arranged_problems = top_line.rstrip() + '\n' + middle_line.rstrip() + '\n' + bottom_line.rstrip()
    if result_line:
        arranged_problems += '\n' + result_line.rstrip()

    return arranged_problems

print(arithmetic_arranger(['235 + 52', '11 + 3', '1002 + 5', '1002 + 6', '5024 + 1002'], True))
