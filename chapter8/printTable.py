tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):

    colsMax = []
    #find col width per col
    for i in range(len(data)):

        colsMax.append(len(data[i][0]))

        for j in range(len(data[i])):

            if len(data[i][j]) > colsMax[i]:
                colsMax[i] = len(data[i][j])

    
    
    index = 0

    while index < len(data[0]):

        for i in range(len(data)):
            print(data[i][index].rjust(colsMax[i]), end=" ")
        print()

        index += 1





        
printTable(tableData)