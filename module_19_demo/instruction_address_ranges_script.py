# Ghidra Scripting: Instructions
# @category: GhidraScripting
# @author: Junjie Zhang

# get address, min address, max address, and the length of an instruction
# the address is the same to the min address
# the length of an instruction is the number of bytes for this instruction
myFunc = getFunctionContaining(currentAddress)
if myFunc:
    fbody = myFunc.getBody() #fbody is an object of AddressSetView
    print(myFunc)
    myListing = currentProgram.getListing()
    instructionIterator = myListing.getInstructions(fbody, True)
    for inst in instructionIterator:
        operands = inst.getInputObjects()
        print(inst)
        print("address: {}, min_address: {}, max_address: {}, size: {}".format(inst.getAddress(), inst.getMinAddress(), inst.getMaxAddress(), inst.getLength()))