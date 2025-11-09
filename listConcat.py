def listConcat(list):
    if len(list) == 0 or len(list) == 1:
        return "List too short"

    new_string = list[0]
    new_string = new_string + ', '
    
    for i in range(1, len(list)):

        new_string = new_string + list[i] + ', '

        if i == len(list) - 2:
            new_string = new_string + 'and ' + list[i+1]
            break
        
    return new_string

    

    


spam = ['apples', 'bananas', 'tofu', 'cats']
print(listConcat(spam))