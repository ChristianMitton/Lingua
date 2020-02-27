import get_closing_bracket
from get_closing_bracket import getClosingBracket

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
                functionEnd = getClosingBracket(filePath, functionStart)                
                                
                return (functionStart, functionEnd)

# def handleFunctionCall(arrayOfArguments, functionBounds):