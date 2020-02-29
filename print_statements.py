def getVariableValue(value, variable_hashtable):
    # count = 1
    # for value in expressionArray[2:]:
    #     # print(f'expression array{count}: {expressionArray}')
    #     # check if value is in variable_hashtable
    #     # remove period if it has one
    #     # value = value.replace(".","")
    #     # words = [w.replace('[br]', '<br />') for w in words]
    if(value in variable_hashtable.keys()):
        variable_value = variable_hashtable[value]
        # expressionArray = [v.replace(value, variable_value) for v in expressionArray]
    # count+=1
    # print(f'returning: {expressionArray}')
    return variable_value

def handlePrintToTerminal(itemToPrint, variable_hashtable):

    itemToPrint = itemToPrint.replace('.','')

    result = getVariableValue(itemToPrint, variable_hashtable)

    print(result)