import sys

def getEndLineNumber(filePath, start_line_number):
    f = open(filePath)
    contents = f.readlines()
    contents = [x.strip() for x in contents] 

    stack = []
    
    line_count = start_line_number
    
    # start from beginning of the line where function is
    for line_number,item in enumerate(contents[start_line_number-1:]):     
    # for item in enumerate(contents[start_line_number-1:]):     
        last_item = item[len(item)-1:]
        # print(last_item)
        if(last_item == '{'):
            stack.append('{')
        elif (last_item == '}'):
            stack.pop()
        
        if(len(stack) < 1):
            return line_count
        line_count += 1

    return 0    

def getFunctionBounds(filePath, functionName):
    f = open(filePath, "r")
    contents = f.readlines()

    # file_lines = convertFileToArray(filePath)

    line_number = 0
    for line in contents:        
        # split line into array
        splitLine = line.split()        

        line_number += 1

        # check if first index has 'create'
        if(len(splitLine) > 0 and splitLine[0] == 'create'): 
            # check if at line of correct function            
            currentFuncName = splitLine[4]
            lastIndex = len(currentFuncName)-1
            
            if(currentFuncName[lastIndex] == '.'):
                currentFuncName = currentFuncName[:-1]

            if(currentFuncName == functionName):                                                
                functionStart = line_number
                f.close()
                functionEnd = getEndLineNumber(filePath, functionStart)                
                                
                return (functionStart, functionEnd)

def getIfStatementBounds(filePath, start_line_number):
    variables = []

    f = open(filePath, "r")
    contents = f.readlines()

    # file_lines = convertFileToArray(filePath)

    line_number = 0
    for line in contents:        
        # split line into array
        splitLine = line.split()        

        line_number += 1

        # check if first index has 'create'
        if(len(splitLine) > 0 and splitLine[0] == 'if'): 
            # check if at line of correct statement            
            # currentFuncName = splitLine[4]
            argument1 = splitLine[1]
            argument2 = splitLine[3]

            # remove comma from arg2
            lastIndex = len(argument2)-1            
            if(argument2[lastIndex] == ','):
                argument2 = argument2[:-1]

            statement_end_line_number = getEndLineNumber(filePath, start_line_number)                
                                
            return (start_line_number, statement_end_line_number, argument1, argument2)

# def handleFunctionCall(arrayOfArguments, functionBounds):
    
# def handleWhileLoop(arrayOfArguments):    


def handleVariableArithmetic(var1, operator, var2):
    if(operator == '+'):        
        result = var1 + var2
    if(operator == '-'):
        result = var1 - var2
    if(operator == '/'):
        result = var1 / var2
    if(operator == '*'):
        result = var1 * var2
    return result
        

def handleIfStatement(filePath, boundsAndArgs):
    f = open(filePath)
    contents = f.readlines()
    contents = [x.strip() for x in contents]

    start, end, arg1, arg2 = boundsAndArgs    
    print(f'if statement start: {start}\nIf statement end: {end}\nArg1: {arg1}\nArg2: {arg2}')

    # start from beginning of the line where function is
    line_count = start
    for item in enumerate(contents[start-1:]):
        line = item[1]

        # print(line)

        # split line
        splitLine = line.split() 
        print(splitLine)
        

        line_count+=1
        if(line_count == end):
            break
        
        # print(line_count)
    


def handlePrintToTerminal(itemToPrint):
    print(itemToPrint)


# TODO: start at main in user file
def main():
    # filename = sys.argv[1]  
    filename = 'test.rr'      
            
    functionBounds = getFunctionBounds(filename, 'foobar')

    functionStart, functionEnd = functionBounds

    # print(f'Funtion start: {functionStart}\nFunction end: {functionEnd}')

    ifStatementBoundsAndArgs = getIfStatementBounds(filename,8)    

    handleIfStatement(filename, ifStatementBoundsAndArgs)        

main()

# if_statements.func()