# Ghidra Scripting: PCode
# @category: GhidraScripting
# @author: Junjie Zhang

cnt = 0
myListing = currentProgram.getListing()
instructionIterator = myListing.getInstructions(True)
for inst in instructionIterator:
    
    cnt += 1
    if cnt > 1000:
        break #only display the first few instructions.
    
    pcodeList = inst.getPcode()
    print("{}".format(inst))
    for pcode in pcodeList:
        print("\t{}".format(pcode))
        print("\t\topcode in integer and in string: {}, {}".format(pcode.getOpcode(), pcode.getMnemonic()))

print("the opcode string for 1 is {}".format(pcode.getMnemonic(1)))
print("the opcode integer for INT_EQUAL is {}".format(pcode.getOpcode("INT_EQUAL")))