# Ghidra Scripting: Instructions
# @category: GhidraScripting
# @author: Junjie Zhang

myFunc = getFunctionContaining(currentAddress)

if myFunc:
    print(myFunc)
    fbody = myFunc.getBody() #fbody is an object of AddressSetView
    myListing = currentProgram.getListing()
    instructionIterator = myListing.getInstructions(fbody, True) # myListing.getInstructions(AddressSetView, Boolean) will return instructions that are inside this set of addresses
    for inst in instructionIterator:
        print("address: {}, instruction: {}".format(inst.getAddress(), inst))