import math
from itertools import combinations

def getData():
    data_list = []
    input_data = open("C:\\Projects\\Tasks\\MinTriangleTask\\input.txt", "r")

    for line in input_data:
        data_list.append(int(line))
        
    input_data.close()
    return data_list
   
def isTriangle(a, b, c):
    return not (a + b < c or a + c < b or b + c < a)

def getArea(a, b, c):
    s = (a + b + c) / 2
    return (s*(s-a)*(s-b)*(s-c)) ** 0.5
    

def calculate():
    data = getData()
    
    all_possible = list(map(tuple, combinations(data, 3)))
    areas = []
    
    for a, b, c in all_possible:
        if isTriangle(a, b, c):
            areas.append(((getArea(a, b, c)), (a,b,c)))
            
    output_data = open("C:\\Projects\\Tasks\\MinTriangleTask\\output.txt", "w")
    output_data.write(str(min([s for f, s in areas])))
    output_data.close()

calculate()
print('Done')