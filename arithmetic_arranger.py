from arithmetic_operator import arithmetic_operator

def arithmetic_arranger(problems, showAns = False):
  arranged_problems = ''
  tmpA = ''
  tmpB = ''
  tmpC = ''
  tmpD = ''

  if (len(problems) > 5): return "Error: Too many problems."

  for problem in problems:
    arOperation = problem.split(' ', 3)
    firstNum = arOperation[0]
    lastNum = arOperation[2]
    sign = arOperation[1]

    if (len(firstNum) > 4 or len(lastNum) > 4):
      return "Error: Numbers cannot be more than four digits."

    if (sign != '+' and sign != '-'): 
      return "Error: Operator must be '+' or '-'."

    try:
      int(firstNum)
      int(lastNum)
    except:
      return "Error: Numbers must only contain digits."
  
  for problem in problems:
    # Pass the value down to the arithmetic_operator function.
    tmpArr = arithmetic_operator(problem)
    # If not the first string in line, add 4 spaces.
    tmpA = (tmpA + 4 * ' ' + tmpArr[0]) if tmpA != '' else tmpArr[0]
    tmpB = (tmpB + 4 * ' ' + tmpArr[1]) if tmpB != '' else tmpArr[1]
    tmpC = (tmpC + 4 * ' ' + tmpArr[2]) if tmpC != '' else tmpArr[2]
    tmpD = (tmpD + 4 * ' ' + tmpArr[3]) if tmpD != '' else tmpArr[3]
  
  # The answer is calculated regadless
  # It's only shown if showAns is set to True
  if showAns:
    arranged_problems = (tmpA + '\n' + tmpB + '\n' + tmpC + '\n' + tmpD)
  else:
    arranged_problems = (tmpA + '\n' + tmpB + '\n' + tmpC)

  return arranged_problems
