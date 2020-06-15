# NAND -> Tetris Assembler - Joe Leveille

import sys
inFileName = sys.argv[1]         #Use first command line arg as name of input file
inFile = open(inFileName,"r")     
lines = inFile.readlines()      #populate lines with strings from each line
inFile.close()  #close file - all data is in lines

for i in range(len(lines)):     #scroll through each line of original file
    lines[i] = lines[i][0:len(lines[i])-1] #remove newline from each line
    lines[i] = str(lines[i]).replace(" ","")    #removes whitespace within line
    if(lines[i].find("//")>-1):     #if a comment is present,
        lines[i] = lines[i][:lines[i].find("//")] #remove the commented portion
lines = [i for i in lines if i]    #remove blank lines

#Now each line will be stripped down to only the code that can be interpreted
instructs = []

for i in range(len(lines)):     #every line of pared down file
    currInst = "0000000000000000" #16 zeros to start each instruction fresh
    if(lines[i].find("@")!=0):
        currInst[0]=1



    instructs.append(currInst)

testStr = "asdfasdf"
print(testStr[3])

for i in range(len(lines)):
    print(lines[i])
print("\n")
for i in range(len(instructs)):
    print(instructs[i])