# NAND -> Tetris Assembler - Joe Leveille

import sys
inFileName = sys.argv[1]         #Use first command line arg as name of input file
inFile = open(inFileName,"r")     
lines = inFile.readlines()      #populate lines with strings from each line
for i in range(len(lines)):     #scroll through each line of file
    if(i!=len(lines)-1):        #if not last line,
        lines[i] = lines[i][0:len(lines[i])-1] #remove newline from each line
    lines[i] = str(lines[i]).replace(" ","")    #removes whitespace within line
inFile.close()  #close file - all data is in lines


print(lines[0])
print(lines[1])
print(lines[2])