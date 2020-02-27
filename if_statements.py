import get_closing_bracket
from get_closing_bracket import getClosingBracket

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

            statement_end_line_number = getClosingBracket(filePath, start_line_number)                
                                
            return (start_line_number, statement_end_line_number, argument1, argument2)

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