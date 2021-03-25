def arithmetic_operator(problem):
  arOperation = problem.split(' ', 3)
  firstNum = arOperation[0]
  lastNum = arOperation[2]
  sign = arOperation[1]
  long = 0
  
  summ = int(firstNum) + int(lastNum) if sign == '+' else int(firstNum) - int(lastNum)

  if len(firstNum) > len(lastNum):
    long = len(firstNum)
  elif len(lastNum) >= len(firstNum):
    long = len(lastNum)
  
  return(
    firstNum.rjust(long + 2),
    (sign.ljust(2) + lastNum.rjust(long)),
    ('-' * (long + 2)),
    str(summ).rjust(long + 2)
  )
