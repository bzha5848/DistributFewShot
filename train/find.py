import os
import csv
def fileFind():
    files = []
    count = 0
    for i in os.listdir("./labels"):
        if i.endswith('.txt'):
            files.append(i)
    for item in files:

        file_data = []
        temp = []


        with open("./labels"+'/'+item, 'r') as myFile:
            is_here = False
            for line in myFile:
                currentLine = line[:-1]
                data = currentLine.split(" ")
              
                for i in data:
                    if i.isdigit():
                        temp = float(i)
                        i = str(int(temp))
                        num: int = int(i)
                        if (num == 14) :
                            print(item)
                            
            if is_here:
                count = count+1
fileFind()