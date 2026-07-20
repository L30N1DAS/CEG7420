# Ghidra Scripting: P-Code
# @category: GhidraScripting
# @author: Junjie Zhang

cnt = 0
myListing = currentProgram.getListing()
instructionIterator = myListing.getInstructions(True)
for inst in instructionIterator:
    cnt += 1
    if cnt > 9:
        break # only display the first few instructions.
    pcodeList = inst.getPcode()
    print("{}".format(inst))
    for pcode in pcodeList:
        print("\t\t{}".format(pcode))