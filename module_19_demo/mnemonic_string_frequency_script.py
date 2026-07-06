# Ghidra Scripting: Instructions
# @category: GhidraScripting
# @author: Junjie Zhang

# This example is to count the occurence for each mnemonic string showing up in this body of the current function.
myDict = {}

myFunc = getFunctionContaining(currentAddress)
if myFunc:
    print(myFunc)
    fbody = myFunc.getBody() #fbody is an object of AddressSetView
    myListing = currentProgram.getListing()
    instructionIterator = myListing.getInstructions(fbody, True) # myListing.getInstructions(AddressSetView, Boolean) will return instructions that are inside this set of addresses
    for inst in instructionIterator:
        mnemonic = inst.getMnemonicString()
        if mnemonic in myDict:
            myDict[mnemonic] = myDict[mnemonic] + 1
        else:
            myDict[mnemonic] = 1

print(myDict)