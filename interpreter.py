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

from expr_eval import expression_eval
from functions import getFunctionBounds
from if_statements import getIfStatementBounds
from if_statements import handleIfStatement  
from variables import handleDeclareVariables
from helper_functions import printHashtable
from return_statements import getValueToReturn


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



# TODO: start at main in user file
def main():    
    filePath = 'sample_lingua_code/sample.lg' # filePath = sys.argv[1]  

    #! contains a {'function' : {'variable': 'value'}} mapping
    function_variable_hashtable = {}

    testFunc = 'foo'

    functionStart, functionEnd = getFunctionBounds(filePath, testFunc)      

    #? function_variable_hashtable will be replaced by each functions hashtable
    handleDeclareVariables(filePath, 3, function_variable_hashtable)
    handleDeclareVariables(filePath, 5, function_variable_hashtable)
    handleDeclareVariables(filePath, 7, function_variable_hashtable)
    handleDeclareVariables(filePath, 9, function_variable_hashtable)    

    returnValue = getValueToReturn(filePath, 11, function_variable_hashtable)

    print(f'{testFunc} start: line {functionStart}\n{testFunc} end: line {functionEnd}')  

    print(f'returnvalue: {returnValue}')  

    print('---[function_variable_hashtable]---')
    printHashtable(function_variable_hashtable)
    print('----------------END----------------')
            
    # functionBounds = getFunctionBounds(filePath, 'foobar')

    # functionStart, functionEnd = functionBounds

    # print(f'Funtion start: {functionStart}\nFunction end: {functionEnd}')    

    print('Done')
main()

# if_statements.func()