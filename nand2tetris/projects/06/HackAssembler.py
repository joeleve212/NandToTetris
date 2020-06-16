# NAND -> Tetris Assembler - Joe Leveille

def checkPredef(addStr):
    if(addStr[0]=='R' and addStr[1:].isnumeric()):
        addVal = addStr[1:]
    elif(addStr=="SP"):
        addVal = "0"
    elif(addStr=="LCL"):
        addVal = "1"
    elif(addStr=="ARG"):
        addVal = "2"
    elif(addStr=="THIS"):
        addVal = "3"
    elif(addStr=="THAT"):
        addVal = "4"
    elif(addStr=="SCREEN"):
        addVal = "16384"
    elif(addStr=="KBD"):
        addVal = "24576"
    else:
        addVal = addStr           #this case only for invalid addresses
    return addVal

def interpCInst(instruct,currInst): # step through to check for each bit
    equalLoc = instruct.find('=')
    MLoc = instruct.find('M')   
    if(MLoc-1==instruct.find("JMP")):    #if the 'M' found is within "JMP",
        MLoc = -1                        #there is no legit 'M' on this line
    ALoc = instruct.find('A')
    DLoc = instruct.find('D')

    if(instruct.find('J')+1):   #checks if this is jump instruct
        JLoc = instruct.find('J')
        jumpCode = instruct[JLoc:JLoc+3]    #handle jump instructions later
    else:
        jumpCode = "000"

    if(MLoc>equalLoc):      #a-bit should be 1, assuming proper syntax (not using both A & M)       
        currInst.append('1')
        # usedLoc = MLoc          #usedLoc is location of either A or M, whichever is used in this instruct
    else:
        currInst.append('0')#a-bit set to 0, or not using M
        # usedLoc = ALoc
        if(equalLoc<1):
            #TODO: deal with jump instructs like D; JMP with no '='    and (LOOP) lines
            test = 1
#            print("Invalid Instruction?")
    
    calc = instruct[equalLoc+1:]
    
    if(calc.find(';')>-1):              #cut out jump instruction if there is one
        calc = calc[:calc.find(';')]
#    print(calc + "Is the calculation")
    if(calc=="0"):                                  #This block fills in the c-bits
        currInst.extend(['1','0','1','0','1','0'])
    elif(calc=="1"):
        currInst.extend(['1','1','1','1','1','1'])
    elif(calc=="-1"):
        currInst.extend(['1','1','1','0','1','0'])
    elif(calc=="D"):
        currInst.extend(['0','0','1','1','0','0'])
    elif(calc=="A" or calc=="M"):
        currInst.extend(['1','1','0','0','0','0'])
    elif(calc=="!D"):
        currInst.extend(['0','0','1','1','0','1'])
    elif(calc=="!A" or calc=="!M"):
        currInst.extend(['1','1','0','0','0','1'])
    elif(calc=="-D"):
        currInst.extend(['0','0','1','1','1','1'])
    elif(calc=="-A" or calc=="-M"):
        currInst.extend(['1','1','0','0','1','1'])
    elif(calc=="D+1" or calc=="1+D"):
        currInst.extend(['0','1','1','1','1','1'])
    elif(calc=="A+1" or calc=="1+A" or calc=="M+1" or calc=="1+M"):
        currInst.extend(['1','1','0','1','1','1'])
    elif(calc=="D-1"):
        currInst.extend(['0','0','1','1','1','0'])
    elif(calc=="A-1" or calc=="M-1"):
        currInst.extend(['1','1','0','0','1','0'])
    elif(calc=="D+A" or calc=="A+D" or calc=="M+D" or calc=="D+M"):
        currInst.extend(['0','0','0','0','1','0'])
    elif(calc=="D-A" or calc=="D-M"):
        currInst.extend(['0','1','0','0','1','1'])
    elif(calc=="A-D" or calc=="M-D"):
        currInst.extend(['0','0','0','1','1','1'])
    elif(calc=="A&D" or calc=="D&A" or calc=="M&D" or calc=="D&M"):
        currInst.extend(['0','0','0','0','0','0'])
    elif(calc=="A|D" or calc=="D|A" or calc=="M|D" or calc=="D|M"):
        currInst.extend(['0','1','0','1','0','1'])
    
    #interpret dest bits
    if(ALoc<equalLoc and ALoc>-1):
        currInst.append('1')
    else:
        currInst.append('0')
    if(DLoc<equalLoc and DLoc>-1):
        currInst.append('1')
    else:
        currInst.append('0')
    if(MLoc<equalLoc and MLoc>-1):
        currInst.append('1')
    else:
        currInst.append('0')
        
  #  print(jumpCode)
    #handle jump bits
    if(jumpCode=="000"):
        currInst.extend(['0','0','0'])
    elif(jumpCode=="JGT"):
        currInst.extend(['0','0','1'])
    elif(jumpCode=="JEQ"):
        currInst.extend(['0','1','0'])
    elif(jumpCode=="JGE"):
        currInst.extend(['0','1','1'])
    elif(jumpCode=="JLT"):
        currInst.extend(['1','0','0'])
    elif(jumpCode=="JNE"):
        currInst.extend(['1','0','1'])
    elif(jumpCode=="JLE"):
        currInst.extend(['1','1','0'])
    elif(jumpCode=="JMP"):
        currInst.extend(['1','1','1'])

    return

def interpAInst(instruct, currInst): #take remaining bits as A reg
    instruct=instruct[1:]   #chops off "@"
    if(instruct.isnumeric()):
        #convert number to binary and store in currInst[1..15], currInst[1] = MSB
        instruct = format(int(instruct),'b') #convert to binary
        
    else:
        #predefined symbols
        instruct = checkPredef(instruct)        #check all predefined values
        if(instruct.isnumeric()):               #check if checkPredef returned variable name or number
            instruct = format(int(instruct) ,'b')
        else:
            currInst.append(instruct)
            #print(instruct)        TODO: remove these sort of useless lines
            return
        #TODO: handle variable names
        #print(instruct + "is not a number")

    binLen = len(instruct)
    for i in range(1,16-binLen):
        currInst.append('0')
    for i in range(binLen):
        currInst.append(instruct[i])
    return

def toString(currInst):
    currStr = ""
    for letter in currInst:
        currStr = currStr + letter
    return currStr

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
offset = 0
labelDict = {           #set up all necessary containers
    "START" : 0
}

for i in range(len(lines)):     #every line of pared down file
    for j in range(16):
        currInst.clear()
#        currInst.append('0') #16 zeros to start each instruction fresh
    if(lines[i].find("@")!=0 and lines[i].find("(")!=0):  #detects a- or c- command
        currInst.extend(['1','1','1'])     #Set locs 1 & 2 = 1 as well - match given assembler
        interpCInst(lines[i],currInst)
    else:
        currInst.append('0')
        interpAInst(lines[i], currInst)
    
    if(lines[i].find(")")>-1):   #check for jump markers
        labelDict[lines[i][1:len(lines[i])-1]] = i-offset   
        offset = offset + 1         #adjust offset as more lines are not skipped going to output file
    else:
        instructs.append(toString(currInst))

varLoc = 16     #first location for arbitrary variables
for i in range(len(instructs)):
    if(not instructs[i].isnumeric()):
 #       print(instructs[i])
        if(labelDict.get(instructs[i][1:])):        #bug fix where jumpLoc = NoneType - This happens when using variables as A values that are not jump markers
            jumpLoc = labelDict.get(instructs[i][1:])               
            num = format(int(jumpLoc) ,'b')         #convert jumpLoc to binary value if it's a jump marker
        else:                                       #handle variables as A inputs
            labelDict[instructs[i][1:]] = varLoc    #each new variable will be assigned a value starting at 16
            num = format(varLoc ,'b')                            #grab num value for this var
            varLoc = varLoc + 1                     #increment varLoc for the next one
        
        instructs[i]= instructs[i][0]      #remove all but the 0

        for j in range(15-len(num)):
            instructs[i] = instructs[i] + "0"
        instructs[i] = instructs[i] + num

# for i in range(len(lines)):
#     print(lines[i])
# print("\n")
for i in range(len(instructs)):
    print(instructs[i])
#print(labelDict)