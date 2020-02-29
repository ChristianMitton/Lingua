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


def main():    
    filePath = sys.argv[1]   

    mainStartLine, mainEndLine = getMainFunctionBounds(filePath)

    executeFunction(filePath, mainStartLine, mainEndLine)    
    
main()