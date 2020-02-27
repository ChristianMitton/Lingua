def getValueToReturn(filePath, line_number, variable_hashtable):
    f = open(filePath, "r")
    contents = f.readlines()
    contents = [x.strip() for x in contents]


    # file_lines = convertFileToArray(filePath)

    line_count = 0
    for line in contents:     
        line_count += 1
        line = line.replace(".","")
        splitLine = line.split()    
        # if at correct line    
        if(line_count == line_number):
            valueToReturn = splitLine[1]            
            # check if return value is in hashtable
            if(valueToReturn in variable_hashtable.keys()):
                valueToReturn = variable_hashtable[valueToReturn]            
            f.close()
            # print(f'valueToReturn: {valueToReturn}')
            return valueToReturn        
