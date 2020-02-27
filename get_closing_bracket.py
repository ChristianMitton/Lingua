def getClosingBracket(filePath, start_line_number):
    f = open(filePath)
    contents = f.readlines()
    contents = [x.strip() for x in contents] 

    stack = []
    
    line_count = start_line_number
    
    # start from beginning of the line where function is
    for line_number,item in enumerate(contents[start_line_number-1:]):     
    # for item in enumerate(contents[start_line_number-1:]):     
        last_item = item[len(item)-1:]
        # print(last_item)
        if(last_item == '{'):
            stack.append('{')
        elif (last_item == '}'):
            stack.pop()
        
        if(len(stack) < 1):
            return line_count
        line_count += 1

    return 0    