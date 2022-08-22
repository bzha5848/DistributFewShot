import os
import csv
def fileFind(number, file):
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
                        if (num == number):
                            # print(item)
                            # file.write(item+'\n')
                            is_here = True
                            # count = 0
                            file.write(item+'\n')
            # if is_here:
            #     count = count+1
            #     if count >= 24:
            #         file.write(item+'\n')
            #         count = 0

f = open("fewshots.txt", "w")
# for n in range(0, 80):
# fileFind(22, f)
# fileFind(23, f)
fileFind(2, f)

f.close()
shopping = open("fewshots.txt")
lines = shopping.readlines()
lines.sort()
sorted_lines = sorted(set(lines))
file = open("fewshotsSORT.txt", "w")
file.writelines(sorted_lines)
file.close()
shopping.close()