import sys
import expr_eval
# import functions
import if_statements
import while_loops
import get_closing_bracket
import print_statements
import variables
import helper_functions
import return_statements
# import functions

from expr_eval import expression_eval
# from functions import getFunctionBounds
from if_statements import getIfStatementBounds
from if_statements import handleIfStatement  
# from variables import handleDeclareVariables
from helper_functions import printHashtable
from return_statements import getValueToReturn  
from get_closing_bracket import getClosingBracket   
# from functions import executeFunction
# from functions import getFunctionNames

def lineIsAFunction(lineStringArray):    
    if(lineStringArray[0] == 'create'):
        return True
    return False
    
def lineIsAnIfStatement(lineStringArray):
    if(lineStringArray[0] == 'if'):
        return True
    return False

def lineIsAWhileLoop(lineStringArray):
    if(lineStringArray[0] == 'while'):
        return True
    return False

def lineIsAPrintStatement(lineStringArray):
    if(lineStringArray[0] == 'print'):
        return True
    return False

def lineIsAVariableDecleration(lineStringArray):
    if(lineStringArray[0] == 'let'):
        return True
    return False

def lineIsAReturnStatement(lineStringArray):
    if(lineStringArray[0] == 'return'):
        return True
    return False

def lineIsMainFunction(lineStringArray):
    if(lineStringArray[0] == 'Start'): #'Start the program at this function. It will be called <function name>{ ... }
        return True
    return False

def getFunctionBounds(filePath, functionName):
    f = open(filePath, "r")
    contents = f.readlines()
    contents = [x.strip() for x in contents]


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
    f.close()
# def handleFunctionCall(arrayOfArguments, functionBounds):

def getFunctionNames(filePath):
    f = open(filePath, "r")
    contents = f.readlines()
    contents = [x.strip() for x in contents]

    result = []

    line_number = 0
    for line in contents: 
        line_number += 1

        if(len(line) < 1):
            continue

        line = line.replace('.','')

        splitLine = line.split()

        if(splitLine[0] == 'create'):
            functionName = splitLine[4]
            result.append(functionName)
    return result

def executeFunction(filePath, startLine, endLine):
# def executeFunction(filePath, startLine, endLine, arguments_hashtable):
    f = open(filePath, 'r')
    contents = f.readlines()
    contents = [x.strip() for x in contents]

    hashTable = {}
    # arguments_hashTable

    #! will only encounter lines within function
    line_count = startLine
    for line in contents[startLine:endLine-1]:
        line_count += 1

        if(len(line) < 1):
            continue

        splitLine = line.split()

        # print(f'[functions] splitLine = {splitLine}')
        # print(f'[functions] line_count = {line_count}')

        if(lineIsAVariableDecleration(splitLine)):
            hashTable = variables.handleDeclareVariables(filePath, line_count, hashTable)

        if(lineIsAReturnStatement(splitLine)):
            returnValue = getValueToReturn(filePath, line_count, hashTable)
            # print(f'return value: {returnValue}')
            f.close()
            return returnValue

        if(lineIsAnIfStatement(splitLine)):
            if_statements.handleIfStatement(filePath, line_count, hashTable)
            # ! skip line to end of if statement

        if(lineIsAPrintStatement(splitLine)):
            print_statements.handlePrintToTerminal(splitLine[1], hashTable)

        # print(line)

    f.close()

    # print(f'Hashtable after finishing execute function {hashTable}')

def getFunctionArguments(filePath, lineNumberOfFunction):
    f = open(filePath, 'r')
    contents = f.readlines()
    contents = [x.strip() for x in contents]

    line_count = 0
    for line in contents:
        line_count += 1
        if(line_count == lineNumberOfFunction):
            stringArray = line.split()
    f.close()


    # print(f'String array: {stringArray}')    
    # return

    numArguments = int(stringArray[7])    

    result = []

    if(numArguments == 0):
        return result
    if(numArguments == 1):        
        var = stringArray[9].replace('(','')
        var = var.replace(')','')
        var = var.replace('{','')        
        result.append(var)    
        return result
    if(numArguments > 1):
        arguments = stringArray[9:]

        for var in arguments:            
            var = var.replace('(','')
            var = var.replace(')','')
            var = var.replace('{','')
            # print(f'at var {var}')
            result.append(var)
    return result

        
    
# getFunctionArguments('sample_lingua_code/sample.lg', 26)
# print(1)