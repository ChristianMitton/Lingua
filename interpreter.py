import sys
import expr_eval
import functions
import if_statements
import while_loops
import get_closing_bracket
import print_statements
import variables
import helper_functions
import return_statements
import functions

from expr_eval import expression_eval
from functions import getFunctionBounds
from if_statements import getIfStatementBounds
from if_statements import handleIfStatement  
from variables import handleDeclareVariables
from helper_functions import printHashtable
from return_statements import getValueToReturn  
from get_closing_bracket import getClosingBracket   
from functions import executeFunction
from functions import getFunctionNames

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

# TODO: FIX
# def getLineNumberOfMainFunction(filePath):
#     f = open(filePath, 'r')
#     contents = f.readlines()
#     contents = [x.strip() for x in contents]
#     # file_lines = convertFileToArray(filePath)

#     line_number = 0
#     for line in contents: 
#         line_number += 1
#         if(len(line) < 1):
#             continue
#         splitLine = line.split()

#         # print(f'Split line: {splitLine}')

#         if(splitLine[0] == 'Start'):
#             f.close()
#             return line_number
#     f.close()
#     print('Error: No main function detected.')
#     exit()

def getMainFunctionBounds(filePath):
    f = open(filePath, "r")
    contents = f.readlines()
    contents = [x.strip() for x in contents]

    line_number = 0
    for line in contents:        
        

        line_number += 1

        if(len(line) < 1):
            continue
        # split line into array                
        splitLine = line.split()
        
        if(splitLine[0] == 'Start'):
                                               
            functionStart = line_number
            f.close()
            functionEnd = getClosingBracket(filePath, functionStart)                
                                
            return (functionStart, functionEnd)
    f.close()




# TODO: start at main in user file
def main():    
    filePath = 'sample_lingua_code/sample.lg' # filePath = sys.argv[1]

    function_variable_hashtable = {}      

    mainStartLine, mainEndLine = getMainFunctionBounds(filePath)

    # f = open(filePath, 'r')
    print("Calling execute function...")
    returnStatement = executeFunction(filePath, mainStartLine, mainEndLine)

    print(returnStatement)

    # print(f'Line {line}')
    # print(f'line start {mainStartLine}\nline end {mainEndLine}')

    print('Done')

# def main():    
#     filePath = 'sample_lingua_code/sample.lg' # filePath = sys.argv[1]  

#     #! contains a {'function' : {'variable': 'value'}} mapping
#     function_variable_hashtable = {}

#     testFunc = 'foo'

#     functionStart, functionEnd = getFunctionBounds(filePath, testFunc)      

#     #? function_variable_hashtable will be replaced by each functions hashtable
#     handleDeclareVariables(filePath, 3, function_variable_hashtable)
#     handleDeclareVariables(filePath, 5, function_variable_hashtable)
#     handleDeclareVariables(filePath, 7, function_variable_hashtable)
#     handleDeclareVariables(filePath, 9, function_variable_hashtable)    

#     returnValue = getValueToReturn(filePath, 11, function_variable_hashtable)

#     print(f'{testFunc} start: line {functionStart}\n{testFunc} end: line {functionEnd}')  

#     print(f'returnvalue: {returnValue}')  

#     print('---[function_variable_hashtable]---')
#     printHashtable(function_variable_hashtable)
#     print('----------------END----------------')

#     print('Done')
main()

# if_statements.func()