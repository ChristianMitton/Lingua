import get_closing_bracket
import variables
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

def handleIfStatement(filePath, startLine, variable_hashTable):
    f = open(filePath, 'r')
    contents = f.readlines()
    contents = [x.strip() for x in contents]

    endLine = get_closing_bracket.getClosingBracket(filePath, startLine)
    
    # arguments_hashTable

    #! will only encounter lines within if statement
    atStartOfStatement = True
    line_count = startLine

    for line in contents[startLine-1:endLine]:
        line_count += 1  

        splitLine = line.split()      

        if(atStartOfStatement):
            print(f'line: {splitLine}')
            variable1 = splitLine[1]
            operator = splitLine[2]
            variable2 = splitLine[3]
            variable2 = variable2.replace(',','')
            print(f'variable1: {variable1}')
            print(f'operator: {operator}')
            print(f'variable1: {variable2}')
            expr = variables.replaceVariables([variable1, operator, variable2], variable_hashTable)
            print(f'expr: {expr}')
            atStartOfStatement = False
        

        if(len(line) < 1 or line == '}'):
            continue

        print(line)

        splitLine = line.split()