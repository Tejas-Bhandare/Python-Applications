# custom filter function
def filterX(function_name, data):
    result = []
    for value in data:
        ret = function_name(value)
        if(ret == True):
            result.append(value)
        
    return result

# custom map function
def mapX(function_name, data):
    result = []
    for value in data:
        result.append(function_name(value))
    
    return result

# custom reduce functions
def reduceX(function_name, data):
    result = 0
    for value in data:
        result = function_name(result, value)
    
    return result


