# Ghidra Scripting: Instructions
# @category: GhidraScripting
# @author: Junjie Zhang

myFunc = getFunctionContaining(currentAddress)

if myFunc:
    print(myFunc)
    fbody = myFunc.getBody() # this is the body of the function, it is an AddressSetView, a set of addresses.
    myInstruction = getFirstInstruction(myFunc) # method in FlatProgramAPI
    while myInstruction and fbody.contains(myInstruction.getAddress()): # verify whether the address of this instruction is inside the set of addresses for this function.
        print("address: {}, instruction: {}".format(myInstruction.getAddress(), myInstruction))
        myInstruction = getInstructionAfter(myInstruction)
else:
    print("No function found at {}.".format(currentAddress))