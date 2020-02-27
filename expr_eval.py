def isOperator(char):
    if(char == '+' or char == '-' or char == '*' or char == '/'):
        return True
    return False

def performOp(num1, operator, num2):
    if(operator == '+'):        
        result = num1 + num2
    if(operator == '-'):
        result = num1 - num2
    if(operator == '/'):
        result = num1 / num2
    if(operator == '*'):
        result = num1 * num2
    return result

def expression_eval(expr):
    stack = []    
    expr = expr.replace(" ",'')

    # i = 0
    # while i < len(expr):
    #     char = expr[i]
    #     print(f'i: {i} Current char: {char}')
    #     if(char == ' '):
    #         i += 1
    #         continue

    #     if(len(stack) > 0):
    #         prevVal = stack.pop()
    #         print(f'prevval: {prevVal}')
    #         if(isOperator(prevVal)):                              
    #             stack.append(prevVal)
    #             print(f'prevVal is an operator\t stack {stack}')  
    #         elif(not isOperator(prevVal) and not isOperator(char)):              
    #             print('prevVal is not an operator')       
    #             prevVal += char
    #             stack.append(prevVal)
    #             # stack.append(char)
    #             i += 1
    #             continue
    #         else:
    #             stack.append(prevVal)                
    #     stack.append(char)
    #     i += 1
        


    i = 0
    while i < len(expr):                
        char = expr[i]
        # print(f'i: {i} Current char: {char}')
        if(char == ' '):
            continue
        if(not isOperator(char)):
            # if(prev val is also a number):
            # if(len(stack) > 0 and not isOperator(stack[len(stack) - 1])):
            #    prevVal = stack.pop() 
            #    prevVal += char
            #    stack.append(prevVal)
            #    i+=2
            #    continue
            # else:
                stack.append(char)
        else:            
            operator = char
            i = i+1 
            # print(f'\ti: {i}')
            char = expr[i]
            # print(f'\tnew char: {char}')
            num1 = int(stack.pop())
            num2 = int(char)            
            
            result = performOp(num1, operator, num2)

            # print(f'num1: {num1} op: {operator} num2: {num2} result: {result}')            
            stack.append(str(result))
            # print(f"Stack: {stack}")
                
        i += 1
                             
    # print(stack)
    return stack.pop()

# while True:
expr = '1 + 2 + 3 * 9'
# expression_eval(expr)