# NAND -> Tetris Assembler - Joe Leveille
def interpCInst(instruct): #TODO: step through to check for each bit
    #
    print("C instruct")
    return


def interpAInst(instruct, currInst): #TODO: take remaining bits as A reg
    instruct=instruct[1:]   #chops off "@"
    if(instruct.isnumeric()):
        #convert number to binary and store in currInst[1..15], currInst[1] = MSB
        instruct = format(int(instruct),'b') #convert to binary
        binLen = len(instruct)
        for i in range(1,16-binLen):
            currInst.append('0')
        for i in range(binLen):
            currInst.append(instruct[i])
    else:
        #TODO: handle variable names
        print(instruct + "is not a number")
    return


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
currInst = []
for i in range(len(lines)):     #every line of pared down file
    for j in range(16):
        currInst.clear()
#        currInst.append('0') #16 zeros to start each instruction fresh
    if(lines[i].find("@")!=0):  #detects a- or c- command
        currInst.append('1')     #TODO: maybe set locs 1 & 2 = 1 as well - match given assembler
        interpCInst(lines[i])
    else:
        currInst.append('0')
        interpAInst(lines[i], currInst)

    instructs.append(str(currInst))


for i in range(len(lines)):
    print(lines[i])
print("\n")
for i in range(len(instructs)):
    print(instructs[i])


