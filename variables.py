import expr_eval
import helper_functions

from expr_eval import expression_eval
from helper_functions import printHashtable

# get lineNumber in file as string
def getLineAsSting(filePath, var_line_number):
    f = open(filePath, "r")
    contents = f.readlines()
    contents = [x.strip() for x in contents]
    # file_lines = convertFileToArray(filePath)

    line_number = 1
    for line in contents:   

        if(line_number == var_line_number):
            f.close()
            return line

        line_number += 1
        
# replaces variables with their values in a hashtable
def replaceVariables(expressionArray, variable_hashtable):
    count = 1
    for value in expressionArray[3:]:
        # print(f'expression array{count}: {expressionArray}')
        # check if value is in variable_hashtable
        # remove period if it has one
        # value = value.replace(".","")
        # words = [w.replace('[br]', '<br />') for w in words]
        if(value in variable_hashtable.keys()):
            variable_value = variable_hashtable[value]
            expressionArray = [v.replace(value, variable_value) for v in expressionArray]
        count+=1
    # print(f'returning: {expressionArray}')
    return expressionArray

# main function
def handleDeclareVariables(filePath, var_decleration_line_number, variable_hashtable):
    line = getLineAsSting(filePath, var_decleration_line_number)
    line = line.replace(".","")
    splitLine = line.split()

    # print(f'Split line: {splitLine}')

    # operation needs to be performed
    if(len(splitLine) > 4):        
        #TODO: replacing any variables in expression with their values
        splitLine = replaceVariables(splitLine, variable_hashtable)      
        # concat expression array into string  
        expression = "".join(splitLine[3:])          

        # print(f'passing this string into expr_eval: {expression}')
        # pass expression string to expression_val
        result = expression_eval(expression)

        new_variable = splitLine[1]
        new_value = result
    else:
        new_variable = splitLine[1]
        new_value = splitLine[3]

    variable_hashtable[new_variable] = new_value    

    return variable_hashtable

# hashTable = {}

# handleDeclareVariables('test_files/test.lg', 3,hashTable)
# handleDeclareVariables('test_files/test.lg', 5, hashTable)
# handleDeclareVariables('test_files/test.lg', 7, hashTable)
# handleDeclareVariables('test_files/test.lg', 9, hashTable)

# printHashtable(hashTable)